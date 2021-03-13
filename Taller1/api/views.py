from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from api.serializers import UserSerializer, SongsSerializer, ArtistLikedSerializer
from api.models import User, Songs, ArtistLiked

# Rendering response
from rest_framework.renderers import JSONRenderer

# Pandas stuff
import pandas as pd
import numpy as np
import random

# Logging
import sys
import logging

@api_view(['POST'])
def login(request):
	try:
		user = User.objects.get(user_id = request.data['user_id']) 
		return JsonResponse('Valid user', safe=False,status=status.HTTP_200_OK)
	except:
		return JsonResponse('Not a valid user', safe=False,status=status.HTTP_404_NOT_FOUND)
	
@api_view(['GET'])
def get_user_data(request, user_query_id):
	try:
		user = User.objects.get(user_id = user_query_id)
		serialized_user = UserSerializer(user)
		return JsonResponse(serialized_user.data, safe=False,status=status.HTTP_200_OK)
	except User.DoesNotExist:
		return JsonResponse('Not found', safe=False,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_users(request):
	try:
		users_query = User.objects.all()
		print(users_query)
		serialized_users = UserSerializer(users_query, many=True)
		return JsonResponse(serialized_users.data, safe=False,status=status.HTTP_200_OK)
	except User.DoesNotExist:
		return JsonResponse('Not found', safe=False,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def register(request):
	serializer = UserSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
	else:
		return JsonResponse({'error': 'El usuario que se quiere crear ya existe'}, safe=False, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_recommendations(request, user_id):
	try:
		user = User.objects.get(user_id = user_id)

		if user.is_old_user:
			df_top_for_user = pd.read_csv(f'./Export/{user_id}_top_100.csv')
			min_id, max_id = (10*user.recommendation_frame, 10*(user.recommendation_frame + 1))
			sample = df_top_for_user[['iid','est']][min_id:max_id].to_dict()
			return JsonResponse(sample, safe=False, status=status.HTTP_200_OK)
		else:
			res = get_top_artists_helper(user.user_id)
			return JsonResponse({'results': res}, safe=False, status=status.HTTP_200_OK)

	except User.DoesNotExist:
		return JsonResponse({'error': 'User does not exist'}, safe=False,status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def play_song(request):
	log = []
	payload = request.data
	try:
		uid = payload['user_id']
		tid = payload['track_id']
		song_obj = Songs.objects.get(track_id=tid)
		song_obj.play_count = song_obj.play_count + 1
		song_obj.save()

		try:
			user = User.objects.get(user_id = uid)
			if not like_artist_helper(user.user_id, song_obj.artist_id, True):
				log.append('user was new but failed to like artist')
		except User.DoesNotExist:
			log.append('user entered did not exist')
		except:
			logging.exception('Unkown reason logging')
			log.append('user like artist failed for unknown reason')
		serialized_song = SongsSerializer(song_obj)
		return JsonResponse({'song_update': serialized_song.data, 'log_out': log}, safe=False, status=status.HTTP_202_ACCEPTED)
	except:
		return JsonResponse({'error': 'an error ocurred, could not update the song play count'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def like_artist(request):
	payload = request.data
	try:
		uid = payload['user_id']
		aid = payload['artist_id']
		valid = like_artist_helper(uid, aid, False)
		if valid:
			return JsonResponse({'msg': "was able to update the user's preferences"}, safe=False, status=status.HTTP_202_ACCEPTED)
		else:
			return JsonResponse({'error': "an error ocurred, could not update the user's preferences"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	except:
		return JsonResponse({'error': "an error ocurred, could not update the user's preferences"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def like_artist_helper(uid, aid, counts):
	try:
		al, created = ArtistLiked.objects.get_or_create(user_id=uid, artist_id=aid)
		if counts:
			al.play_count = al.play_count+1
			al.save()
		return True
	except:
		logging.exception('Error for like artist helper')
		return False

def get_top_artists_helper(uid):
	try: 
		artistsLiked = ArtistLiked.objects.all().filter(user_id=uid)
		aid_list = []
		i = 0
		for x in artistsLiked:
			aid_list.append(x.artist_id)
		
		user = User.objects.get(user_id=uid)
		random.seed(user.recommendation_frame)
		random.shuffle(aid_list)

		recommended_aid_list = []
		df_neighbors = pd.read_csv('./Export/webapp_neighbors_map.csv')
		for i in range(0, min(len(aid_list), 10)):
			aid=aid_list[i]
			req = 10
			df_filtered = df_neighbors[aid]
			valid = df_filtered.loc[np.bitwise_not(np.bitwise_or(np.isin(df_filtered, aid_list), np.isin(df_filtered, recommended_aid_list)))]
			for x in valid[aid]:
				req -= 1
				recommended_aid_list.append(x)
				if req == 0:
					break
		
		random.shuffle(recommended_aid_list)
		filtered_res = recommended_aid_list[0:min(len(recommended_aid_list), 10)]
	except:
		logging.exception('Error for top artists helper')
		return False

#TODO: get info from aid
#TODO: get info from tid
#TODO: push recommendation window
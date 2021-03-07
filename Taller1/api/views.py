from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from api.serializers import UserSerializer, InteractionsSerializer, SongsSerializer 
from api.models import User, Interactions, Songs

# Rendering response
from rest_framework.renderers import JSONRenderer

# Pandas stuff
import pandas as pd

# Create your views here.

@api_view(['POST'])
def login(request):
	try:
		user = User.objects.get(user_id = request.data['user_id']) 
		return JsonResponse('se logro', safe=False,status=status.HTTP_202_ACCEPTED)


	except User.DoesNotExist:
		return JsonResponse('no se logro', safe=False,status=status.HTTP_404_NOT_FOUND)
	
@api_view(['GET'])
def get_user_data(request, user_query_id):
	try:
		user = User.objects.get(user_id = user_query_id)
		serialized_entity = UserSerializer(data=user)
		if serialized_entity.is_valid():
			return JsonResponse(JSONRenderer().render(serialized_entity.data), safe=False,status=status.HTTP_200_OK)
		else:
			return JsonResponse(serialized_entity.errors, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	except User.DoesNotExist:
		return JsonResponse('Not found', safe=False,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_users(request):
	try:
		users_query = User.objects.all()
		print(users_query)
		serialized_users = UserSerializer(users_query, many=True)
		if serialized_users.is_valid():
			return JsonResponse(JSONRenderer().render(serialized_users.data), safe=False,status=status.HTTP_200_OK)
		else:
			return JsonResponse(serialized_users.errors, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	except User.DoesNotExist:
		return JsonResponse('Not found', safe=False,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def register(request):
	serializer = UserSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_202_ACCEPTED)
	else:
		return JsonResponse('El usuario que se quiere crear ya existe', safe=False, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_recommendations(request, user_id):
	df_top_for_user = pd.read_csv(f'./Export/{user_id}_top_100.csv')
	sample = df_top_for_user.sample(n=10)[['iid','est']].to_dict()
	return JsonResponse(sample, safe=False, status=status.HTTP_200_OK)

def increase_number_counts(request, song_id):
	print ('')

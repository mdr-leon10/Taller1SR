# serializers.py
from rest_framework import serializers

from api.models import User
from api.models import Songs
from api.models import ArtistLiked

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'identifier', 'is_old_user', 'recommendation_frame']

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['artist_id', 'artist_name', 'track_name', 'track_id', 'play_count', 'identifier']

class ArtistLikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistLiked
        fields = ['identifier', 'artist_id', 'user_id', 'play_count']

class ArtistPlayTotalSerializer(serializers.Serializer):
    artist_id = serializers.CharField()
    play_sum = serializers.IntegerField()

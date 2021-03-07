# serializers.py
from rest_framework import serializers

from api.models import User
from api.models import Interactions
from api.models import Songs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'identifier', 'is_old_user', 'recommendation_frame']

class InteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interactions
        fields = ['identifier', 'artist_id', 'artist_name', 'track_name', 'track_id', 'rating', 'is_explicit', 'count', 'from_user']

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['artist_id', 'artist_name', 'track_name', 'track_id', 'identifier']
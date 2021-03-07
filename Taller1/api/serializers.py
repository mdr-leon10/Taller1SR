# serializers.py
from rest_framework import serializers

from .models import User
from .models import Interactions
from .models import Songs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'identifier')

class InteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interactions
        fields = ('identifier', 'artist_id', 'artist_name', 'track_name', 'track_id', 'rating', 'is_explicit', 'count', 'from_user')

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('artist_id', 'artist_name', 'track_name', 'track_id', 'identifier')
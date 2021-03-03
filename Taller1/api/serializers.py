# serializers.py
from rest_framework import serializers

from .models import User
from .models import interaction
from .models import songs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'identifier')

class InteractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = interaction
        fields = ('artist_id', 'user_id', 'count', 'rating_estandar', 'artist_name')

class SongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songs
        fields = ('artist_id', 'artist_name', 'track_name', 'track_id', 'identifier', 'count')
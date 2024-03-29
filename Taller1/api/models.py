from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=60, unique=True)
	identifier = models.AutoField(primary_key=True)
	is_old_user = models.BooleanField(default=False)
	recommendation_frame = models.IntegerField(default=0)

class Songs(models.Model):
	identifier = models.AutoField(primary_key=True)
	artist_id = models.CharField(max_length=255)
	artist_name = models.CharField(max_length=255)
	track_name = models.CharField(max_length=255)
	track_id = models.CharField(max_length=255)
	play_count = models.PositiveIntegerField(default=0)

class ArtistLiked(models.Model):
	identifier = models.AutoField(primary_key=True)
	user_id = models.CharField(max_length=60)
	artist_id = models.CharField(max_length=255)
	liked = models.BooleanField(default=True)
	play_count = models.PositiveIntegerField(default=0)
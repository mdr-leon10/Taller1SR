from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=60, unique=True)
	identifier = models.AutoField(primary_key=True)
	is_old_user = models.BooleanField(default=False)
	recommendation_frame = models.IntegerField(default=0)

class Interactions(models.Model):
	identifier = models.AutoField(primary_key=True)
	from_song = models.ForeignKey(Songs, on_delete=models.CASCADE)
	from_user = models.ForeignKey(User, on_delete=models.CASCADE)
	count = models.PositiveIntegerField()

class Songs(models.Model):
	identifier = models.AutoField(primary_key=True)
	artist_id = models.CharField(max_length=255)
	artist_name = models.CharField(max_length=255)
	track_name = models.CharField(max_length=255)
	track_id = models.CharField(max_length=255)
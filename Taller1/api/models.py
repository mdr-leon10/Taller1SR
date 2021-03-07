from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=60, unique=True)
	identifier = models.AutoField(primary_key=True)

class Interactions(models.Model):
	identifier = models.AutoField(primary_key=True)
	artist_id = models.CharField(max_length=255)
	artist_name = models.CharField(max_length=255)
	track_name = models.CharField(max_length=255)
	track_id = models.CharField(max_length=255)
	rating = models.FloatField()
	is_explicit = models.BooleanField(default=False)
	count = models.PositiveIntegerField()
	from_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Songs(models.Model):
	identifier = models.AutoField(primary_key=True)
	artist_id = models.CharField(max_length=255)
	artist_name = models.CharField(max_length=255)
	track_name = models.CharField(max_length=255)
	track_id = models.CharField(max_length=255)
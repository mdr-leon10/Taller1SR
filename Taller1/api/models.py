from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=60)
	identifier = models.AutoField(primary_key=True)

class interaction(models.Model):
	artist_id = models.CharField(max_length=255)
	user_id = models.CharField(max_length=255)
	count = models.PositiveIntegerField()
	rating_estandar = models.FloatField()
	artist_name = models.CharField(max_length=255)

class songs(models.Model):
	artist_id = models.CharField(max_length=255)
	artist_name = models.CharField(max_length=255)
	track_name = models.CharField(max_length=255)
	track_id = models.CharField(max_length=255)
	identifier = models.AutoField(primary_key=True)
	count = models.PositiveIntegerField()



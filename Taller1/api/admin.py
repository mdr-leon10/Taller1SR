from django.contrib import admin
from api.models import User
from api.models import Songs
from api.models import ArtistLiked

# Register your models here.
admin.site.register(User)
admin.site.register(ArtistLiked)
admin.site.register(Songs)

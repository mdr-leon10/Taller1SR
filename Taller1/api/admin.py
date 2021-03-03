from django.contrib import admin
from .models import User
from .models import interaction
from .models import songs

# Register your models here.
admin.site.register(User)
admin.site.register(interaction)
admin.site.register(songs)

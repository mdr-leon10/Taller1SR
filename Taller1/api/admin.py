from django.contrib import admin
from .models import User
from .models import Interactions
from .models import Songs

# Register your models here.
admin.site.register(User)
admin.site.register(Interactions)
admin.site.register(Songs)

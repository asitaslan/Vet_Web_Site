from django.contrib import admin

# Register your models here.
from home.models import User, Animal

admin.site.register(User)
admin.site.register(Animal)
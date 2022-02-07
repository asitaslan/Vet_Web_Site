import os

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (BaseUserManager,
                                           AbstractBaseUser)
from django.utils import timezone
import uuid
from django.utils.http import int_to_base36


def get_profile_image_path(instance, filename):
    return os.path.join('Users_Profile_Photos', instance.username, filename)


def get_animal_image_path(instance, filename):
    return os.path.join('Animal_Photos', instance.name, filename)
ID_LENGTH = 20
length = 20
def id_gen() -> str:
    fisrt = int_to_base36(uuid.uuid4().int)[:length]
    return f'{fisrt}'



class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, ' ',
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=15)
    registrationDate = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(blank=True, null=True, upload_to=get_profile_image_path)
    adress = models.CharField(max_length=150, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]


class Animal(models.Model):
    id = models.CharField(max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False)
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=30)
    genus = models.CharField(max_length=30)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to=get_animal_image_path)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'animal:  {self.name}  ----  owner:  {self.owner.username}'

import os
from django.db import models
import uuid
from django.utils.http import int_to_base36
from user.models import User

def get_animal_image_path(instance, filename):
    return os.path.join('Animal_Photos', instance.name, filename)


ID_LENGTH = 20
length = 20
def id_gen() -> str:
    fisrt = int_to_base36(uuid.uuid4().int)[:length]
    return f'{fisrt}'



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

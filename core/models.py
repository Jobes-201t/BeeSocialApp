from django.db import models
from django.contrib.auth import get_user_model

#Creando el primer usario
User = get_user_model()

# Create your models here.

# Creando el primer Modelo paso 5
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
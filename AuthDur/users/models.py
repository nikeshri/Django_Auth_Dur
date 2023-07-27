from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = None



    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import CommonModel

class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, default='C')


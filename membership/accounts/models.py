from django.contrib.auth.models import AbstractUser
from common.models import CommonModel
from django.db import models

class User(AbstractUser, CommonModel):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    toBeBudgeted = models.IntegerField

class Shift(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.amount)


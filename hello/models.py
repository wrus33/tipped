from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    toBeBudgeted = models.IntegerField
    def __str__(self):
        return str(self.user)

class Shift(models.Model):
    predicted = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,verbose_name = 'User',related_name='Shifts', on_delete=models.CASCADE)
    actual = models.IntegerField()
    def variance(self):
        return actual - predicted
    def __str__(self):
        return str(self.predicted)



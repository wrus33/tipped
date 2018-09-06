from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Shift(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return str(self.amount)

from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class testClass(models.Model):
    firstField = models.CharField(max_length=200)
    secondField = models.DateTimeField('date pubished')
    def __str__(self):
        return self.firstField

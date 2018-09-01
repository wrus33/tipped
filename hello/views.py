import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


from .models import Greeting
from .models import testClass
from .models import Shift

# Create your views here.
def index(request):
    testCases = testClass.objects.order_by('secondField')
    shifts = Shift.objects.all()
    return render(request, 'index.html', {'shifts': shifts})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


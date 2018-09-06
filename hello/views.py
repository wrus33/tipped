import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Shift

# Create your views here.
def index(request):
    shifts = Shift.objects.all()
    
    return render(request, 'hello/home.html', {'shifts': shifts})

def scheduled(request):
    shifts = Shift.objects.order_by('date')
    average = Shift.objects.aggregate(Avg('amount'))
    return render(request, 'hello/quickview.html', {'shifts': shifts})

def statistics(request):
    shifts = Shift.objects.all()

    return render(request, 'hello/statistics.html', {'shifts': shifts})

def tip(request, pk):
    tip = get_object_or_404(Shift, pk=pk)
    return render(request, 'hello/tip.html', {'tip': tip})




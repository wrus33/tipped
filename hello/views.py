import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .forms import ShiftForm
from django.shortcuts import redirect
from datetime import datetime

from .models import Shift

def index(request):
    shifts = Shift.objects.all()
    
    return render(request, 'hello/home.html', {'shifts': shifts})

def scheduled(request):
    now = datetime.now()
    shifts = Shift.objects.filter(date__gte=now, user=request.user).order_by('date')
    return render(request, 'hello/tip_list.html', {'shifts': shifts})



def statistics(request):
    shifts = Shift.objects.all()
    return render(request, 'hello/statistics.html', {'shifts': shifts})

def addnew(request):
    if request.method == "POST":
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.predicted = 50
            shift.actual = 0
            shift.user = request.user
            shift.save()
            return redirect('scheduled', )
    else:
        form = ShiftForm()
    return render(request, 'hello/addnew.html', {'form': form})

def shift(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    return render(request, 'hello/shift.html', {'shift': shift})

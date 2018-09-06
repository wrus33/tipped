import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .forms import ShiftForm
from django.shortcuts import redirect

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
    return render(request, 'hello/quickview.html', {'form': form})

def addnew(request):
    if request.method == "POST":
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.amount = 50
            shift.user = 1;
            shift.save()
            return redirect('scheduled', )
    else:
        form = ShiftForm()
    return render(request, 'hello/addnew.html', {'form': form})

def tip(request, pk):
    tip = get_object_or_404(Shift, pk=pk)
    return render(request, 'hello/tip.html', {'tip': tip})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

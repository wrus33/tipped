from django import template
from django.db.models import Avg, Sum
from hello.models import Shift
from datetime import datetime
from django.utils import timezone


register = template.Library()
now = datetime.now()

@register.simple_tag
def count():
	return Shift.objects.filter(date__gte=now).count()


@register.simple_tag
def avg():
	return Shift.objects.filter(date__gte=now).aggregate(Avg('predicted'))


@register.simple_tag
def total():
	return Shift.objects.filter(date__gte=now).aggregate(Sum('predicted'))

@register.simple_tag
def monthToDate():
	return Shift.objects.filter(date__lt=now).aggregate(Sum('actual'))
	

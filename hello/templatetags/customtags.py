from django import template
from django.db.models import Avg, Sum
from hello.models import Shift


register = template.Library()

@register.simple_tag
def count():
	return Shift.objects.count()

@register.simple_tag
def avg():
	return Shift.objects.aggregate(Avg('amount'))

@register.simple_tag
def total():
	return Shift.objects.aggregate(Sum('amount'))



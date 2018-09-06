from django import template
from django.db.models import Avg
from ..models import Shift


register = template.Library()

@register.simple_tag
def avg():
	average = Shift.objects.aggregate(Avg('amount'))
	return average
from django import forms

from .models import Shift
from.models import User

class ShiftForm(forms.ModelForm):

    class Meta:
        model = Shift
        fields = ('date',)



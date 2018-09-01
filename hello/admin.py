from django.contrib import admin

from .models import testClass
from .models import Shift

admin.site.register(testClass)
admin.site.register(Shift)


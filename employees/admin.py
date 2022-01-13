from django.contrib import admin
from .models import Employees, Banks, Countries
# Register your models here.

admin.site.register(Employees)
admin.site.register(Banks)
admin.site.register(Countries)


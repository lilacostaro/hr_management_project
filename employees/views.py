from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Countries, Regions

# Create your views here.
def index(request):
    countries_list = Countries.objects.all()
    regions_list = Regions.objects.all()
    template = loader.get_template('employees/index.html')
    context = {
        'countries_list': countries_list,
        'regions_list': regions_list
    }
    return HttpResponse(template.render(context, request))
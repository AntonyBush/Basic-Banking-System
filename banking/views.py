from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
def home(request):
    return render(request,'base.html')
    
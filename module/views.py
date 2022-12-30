from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from . import models
# Create your views here.

# rendert die base.html
def index(request):
    return render(request, 'module/base.html')

def einfuehrung(request, modul_id, unterseite_id):
    modul = models.Modul.objects.get(nummer=modul_id)
    unterseite = models.Unterseite.objects.get(nummer=unterseite_id, modul = modul)
    
    return render(request, 'users/einfuehrung.html', {'modul': modul, 'unterseite' : unterseite})
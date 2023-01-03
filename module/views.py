from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from . import models
# Create your views here.

# rendert die index.html
def index(request):
    return render(request, 'module/index.html')

# rendert die modulseite.html
def modulseite(request, modul_id, unterseite_id):
    modul = models.Modul.objects.get(nummer=modul_id)
    unterseite = models.Unterseite.objects.get(nummer=unterseite_id, modul = modul)
    
    return render(request, 'module/modulseite.html', {'modul': modul, 'unterseite' : unterseite})

def einfuehrung(request, unterseite_id):
    modul_id = 0
    modul = models.Modul.objects.get(nummer=modul_id)
    unterseite = models.Unterseite.objects.get(nummer=unterseite_id, modul = modul)
    
<<<<<<< Local Changes
<<<<<<< Local Changes
    return render(request, 'module/einfuehrung.html', {'modul': modul, 'unterseite' : unterseite})

def quiz(request, modul_id, frage_id, ):
    modul = models.Modul.objects.get(nummer=modul_id)
    unterseite = models.Unterseite.objects.get(nummer=unterseite_id, modul = modul)
    
    return render(request, 'module/quiz.html', {'modul': modul, 'unterseite' : unterseite})=======
    return render(request, 'module/einfuehrung.html', {'modul': modul, 'unterseite' : unterseite})>>>>>>> External Changes
=======
    return render(request, 'module/einfuehrung.html', {'modul': modul, 'unterseite' : unterseite})

def quiz(request, modul_id, unterseite_id):
    modul = models.Modul.objects.get(nummer=modul_id)
    unterseite = models.Unterseite.objects.get(nummer=unterseite_id, modul = modul)
    
    return render(request, 'module/quiz.html', {'modul': modul, 'unterseite' : unterseite})>>>>>>> External Changes

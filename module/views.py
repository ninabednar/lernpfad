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
    
    return render(request, 'module/einfuehrung.html', {'modul': modul, 'unterseite' : unterseite})

def quiz(request, modul_id, frage_id):
    modul = models.Modul.objects.get(nummer=modul_id)
    frage = models.Frage.objects.get(frage_id=frage_id, modul = modul)
    antworten =  models.Antwort.objects.filter(frage=frage)
    antwortliste = []
    for antwort in antworten:
        antwortliste.append(antwort)
    
    return render(request, 'module/quiz.html', {'modul': modul, 'frage' : frage, 'antwortliste': antwortliste})

def ergebnis(request, modul_id, frage_id):
    modul = models.Modul.objects.get(nummer=modul_id)
    frage = models.Frage.objects.get(frage_id=frage_id, modul = modul)
    antworten =  models.Antwort.objects.filter(frage=frage)
    antwortliste = []
    for antwort in antworten:
        antwortliste.append(antwort)
    
    return render(request, 'module/ergebnis.html', {'modul': modul, 'frage' : frage, 'antwortliste': antwortliste})

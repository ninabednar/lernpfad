from django.contrib import admin
from .models import Patient, Modul, Frage, Antwort
# Register your models here.

admin.site.register(Patient)
admin.site.register(Modul)
admin.site.register(Frage)
admin.site.register(Antwort)
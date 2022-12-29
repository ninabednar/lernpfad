from django.contrib import admin
from .models import Modul, Unterseite, Frage, Antwort
# Register your models here.
admin.site.register(Modul)
admin.site.register(Unterseite)
admin.site.register(Frage)
admin.site.register(Antwort)

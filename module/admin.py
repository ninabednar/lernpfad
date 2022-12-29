from django.contrib import admin
from .models import Modul, Unterseite, Frage, Antwort
# Register your models here.
class UnterseiteAdmin(admin.ModelAdmin):
    list_filter = ['modul']

class FrageAdmin(admin.ModelAdmin):
    list_filter = ['modul']
    
class AntwortAdmin(admin.ModelAdmin):
    list_filter = ['frage', 'richtige_loesung']
    
admin.site.register(Modul)
admin.site.register(Unterseite, UnterseiteAdmin)
admin.site.register(Frage, FrageAdmin)
admin.site.register(Antwort, AntwortAdmin)
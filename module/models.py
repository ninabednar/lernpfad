from django.db import models

# Create your models here.
class Modul(models.Model):
    name = models.CharField(max_length=30)
    nummer = models.IntegerField(default=0)
    class Meta:
            verbose_name_plural = "module"
    def __str__(self):
        return str(self.nummer) + ' | ' + self.name #In Admin-Oberfläche wird Name des Moduls angezeigt
        
class Frage(models.Model):
    frage_id = models.IntegerField(default=0)
    frage_titel = models.CharField(max_length=200, default='')
    frage_satz = models.TextField(max_length=200)
    frage_modul = models.ForeignKey(Modul, on_delete=models.CASCADE)
    erklaerung = models.TextField(max_length=1000, blank=True, default='')
    class Meta:
            verbose_name_plural = "fragen"
    def __str__(self):
        return str(self.frage_modul) + ' | ' + self.frage_titel #In Admin-Oberfläche wird Fragetitel und ID der Frage gezeigt

class Antwort(models.Model):
    antwort_id = models.IntegerField(default=0)
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE) #Greift auf vorhandene Fragen zu
    antwort_text = models.TextField(max_length=200)
    richtige_loesung = models.BooleanField(default=False)
    class Meta:
            verbose_name_plural = "antworten"
    def __str__(self):
        return str(self.frage) + ' - ' + str(self.antwort_text)
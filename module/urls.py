"""prototyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'module'
urlpatterns = [
    #path('', views.index, name='index'),
    path('einfuehrung/<int:unterseite_id>/', views.einfuehrung, name='einführung'),
    path('<int:modul_id>/<int:unterseite_id>/', views.modulseite, name='modulseite'),
    path('quiz/<int:modul_id>/<int:frage_id>/', views.quiz, name='quiz'),
    path('ergebnis/<int:modul_id>/<int:frage_id>/', views.ergebnis, name='ergebnis'),
    #path('module/', include('module.urls')),
    #path('', views.index, name='index'),

]
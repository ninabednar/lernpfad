from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
]
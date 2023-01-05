from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('onboarding/<int:ident>/', views.onboarding, name='onboarding'),
]
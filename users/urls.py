from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.index, name='index'),
    path('users/', include('users.urls')),
    #path('members/', views.members, name='members'),
]
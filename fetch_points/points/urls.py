from django.urls import path

from . import views

app_name = 'points'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('spend/', views.spend, name='spend'),
    path('balance/', views.balance, name='balance'),
]
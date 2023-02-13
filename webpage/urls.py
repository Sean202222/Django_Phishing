from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('recc', views.recc, name='recc'),
    path('phish1', views.phish1, name='phish1'),
    path('phish1a', views.phish1a, name='phish1a'),
    path('phish2', views.phish2, name='phish2'),
]
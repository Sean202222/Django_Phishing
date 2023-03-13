from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('recc', views.recc, name='recc'),
    path('phish1', views.phish1, name='phish1'),
    path('phish1a', views.phish1a, name='phish1a'),
    path('phish1b', views.phish1b, name='phish1b'),
    path('phish1c', views.phish1c, name='phish1c'),
    path('phish2', views.phish2, name='phish2'),
    path('phish3', views.phish3, name='phish3'),
]
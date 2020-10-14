from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('newproject/', views.newproject, name='newproject'),
    path('project/', views.project),
    path('addfeature/', views.addfeature),
    path('featureoverview/', views.featureoverview),
    path('add_attribute/', views.add_attribute),
]

from django.urls import path, include
from manga import views

urlpatterns = [
    path('', views.index),
]
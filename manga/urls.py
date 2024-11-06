from django.urls import path, include
from manga import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>/', views.detail_view, name='detail')
]
from django.urls import path, include
from manga import views

urlpatterns = [
    path('', views.index),
    path('<str:cate>/', views.filterByCate),
    path('detail/<int:id>', views.detail_view, name='detail'),
    path('ep/<int:id>', views.detailEpisode),
    path('/test', views.manga),


]
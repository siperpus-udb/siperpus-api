from django.urls import path
from . import views

urlpatterns = [
    path('buku/', views.BukuList.as_view(), name='buku-list'),
    path('buku/<pk>/', views.BukuDetail.as_view(), name='buku-detail'),
]
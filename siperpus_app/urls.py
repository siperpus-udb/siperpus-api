from django.urls import path
from . import views

urlpatterns = [
    path('buku/', views.BookList.as_view(), name='buku-list'),
    path('buku/<pk>/', views.BookDetail.as_view(), name='buku-detail'),
]
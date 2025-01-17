from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
    path('new-books/', views.NewBookList.as_view(), name='newBook-list'),
    path('new-books/<pk>/', views.NewBookDetail.as_view(), name='newBook-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('authors/<pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('new-books/', views.NewBookList.as_view(), name='newBook-list'),
    path('new-books/<pk>/', views.NewBookDetail.as_view(), name='newBook-detail'),
]
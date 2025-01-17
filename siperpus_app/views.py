from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from siperpus_app.models import Buku, Penerbit, BukuMasuk
from siperpus_app.serializers import BookSerializer, AuthorSerializer, NewBookSerializer

class BookList(APIView):
    def post(self, request):
        books = BookSerializer(data=request.data, context={'request': request})
        if books.is_valid():
            books.save()
            return Response(books.data, status=status.HTTP_201_CREATED)

        return Response(books.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        books = Buku.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response({
            "books": serializer.data,
        }, status.HTTP_200_OK)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Buku.objects.get(pk=pk)
        except Buku.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        books = self.get_object(pk)
        serializer = BookSerializer(books)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        books = self.get_object(pk)
        serializer = BookSerializer(books, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        books = self.get_object(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorList(APIView):
    def post(self, request):
        authors = AuthorSerializer(data=request.data, context={'request': request})
        if authors.is_valid():
            authors.save()
            return Response(authors.data, status=status.HTTP_201_CREATED)

        return Response(authors.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        authors = Penerbit.objects.all()
        serializer = AuthorSerializer(authors, many=True, context={'request': request})
        return Response({
            "authors": serializer.data,
        }, status.HTTP_200_OK)

class AuthorDetail(APIView):
    def get_object(self, pk):
        try:
            return Penerbit.objects.get(pk=pk)
        except Penerbit.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        authors = self.get_object(pk)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        authors = self.get_object(pk)
        serializer = AuthorSerializer(authors, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        authors = self.get_object(pk)
        authors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NewBookList(APIView):
    def post(self, request):
        newBooks = NewBookSerializer(data=request.data, context={'request': request})
        if newBooks.is_valid():
            newBooks.save()
            return Response(newBooks.data, status=status.HTTP_201_CREATED)

        return Response(newBooks.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        newBooks = BukuMasuk.objects.all()
        serializer = NewBookSerializer(newBooks, many=True, context={'request': request})
        return Response({
            "new-books": serializer.data,
        }, status.HTTP_200_OK)

class NewBookDetail(APIView):
    def get_object(self, pk):
        try:
            return BukuMasuk.objects.get(pk=pk)
        except BukuMasuk.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        newBooks = self.get_object(pk)
        serializer = NewBookSerializer(newBooks)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        newBooks = self.get_object(pk)
        serializer = NewBookSerializer(newBooks, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newBooks = self.get_object(pk)
        newBooks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from siperpus_app.models import Buku
from siperpus_app.serializers import BookSerializer

# Create your views here.
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
            "buku": serializer.data,
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
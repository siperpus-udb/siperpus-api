from unittest import expectedFailure

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from siperpus_app.models import Buku
from siperpus_app.serializers import BukuSerializer

# Create your views here.
class BukuList(APIView):
    def post(self, request):
        buku = BukuSerializer(data=request.data, context={'request': request})
        if buku.is_valid():
            buku.save()
            return Response(buku.data, status=status.HTTP_201_CREATED)

        return Response(buku.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        buku = Buku.objects.all()
        serializer = BukuSerializer(buku, many=True, context={'request': request})
        return Response({
            "buku": serializer.data,
        }, status.HTTP_200_OK)

class BukuDetail(APIView):
    def get_object(self, pk):
        try:
            return Buku.objects.get(pk=pk)
        except Buku.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        buku = self.get_object(pk)
        serializer = BukuSerializer(buku)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        buku = self.get_object(pk)
        serializer = BukuSerializer(buku, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        buku = self.get_object(pk)
        buku.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
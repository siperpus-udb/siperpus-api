from django.db import models
from django.db.models import Model


# Create your models here.
class Buku(models.Model):
    idbuku = models.AutoField(primary_key=True)
    harga = models.PositiveIntegerField(default=0)
    nama = models.CharField(max_length=255)
    stok = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Penerbit(models.Model):
    idpenerbit = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nohp = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BukuMasuk(models.Model):
    idtrans = models.AutoField(primary_key=True)
    idbuku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    idpenerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
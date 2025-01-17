from rest_framework import serializers
from rest_framework.reverse import reverse

from siperpus_app.models import Buku, Penerbit, BukuMasuk


class BookSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Buku
        fields = ['idbuku', 'nama', 'harga', 'stok', 'created_at', 'updated_at', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('book-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('book-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('book-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('book-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "DELETE",
                "types": ["application/json"]
            },

        ]

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Penerbit
        fields = ['idpenerbit', 'nama', 'alamat', 'nohp', 'created_at', 'updated_at', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('author-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('author-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('author-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('author-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]

class NewBookSerializer(serializers.HyperlinkedModelSerializer):
    idbuku = serializers.HyperlinkedRelatedField(
        queryset=Buku.objects.all(),
        view_name='book-detail',  # Ensure this matches the URL name for Buku
        lookup_field='pk',
        required=True  # Ensure this field is required
    )
    idpenerbit = serializers.HyperlinkedRelatedField(
        queryset=Penerbit.objects.all(),
        view_name='author-detail',  # Ensure this matches the URL name for Penerbit
        lookup_field='pk',
        required=True  # Ensure this field is required
    )

    _links = serializers.SerializerMethodField()

    class Meta:
        model = BukuMasuk
        fields = ['idtrans', 'idbuku', 'idpenerbit', 'jumlah', 'created_at', 'updated_at', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('newBook-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('newBook-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('newBook-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('newBook-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]
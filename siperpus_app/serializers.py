from rest_framework import serializers
from rest_framework.reverse import reverse

from siperpus_app.models import Buku

class BukuSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Buku
        fields = ['idbuku', 'nama', 'harga', 'stok', 'created_at', 'updated_at', '_links']

    def get__links(self, obj):
        request =   self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('buku-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('buku-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('buku-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('buku-detail', kwargs={'pk': obj.pk} ,request=request),
                "action": "DELETE",
                "types": ["application/json"]
            },

        ]
import random
from django.core.management.base import BaseCommand
from django.template.smartif import Literal
from faker import Faker
from siperpus_app.models import Buku, Penerbit, BukuMasuk


class Command(BaseCommand):
    help = 'Generate fake data'

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10):
            Buku.objects.create(
                nama=fake.sentence(nb_words=3),
                harga=fake.random_int(50000, 200000, 5000),
                stok=fake.random_int(10, 1000, 8)
            )

        for _ in range(10):
            Penerbit.objects.create(
                nama=fake.company(),
                alamat=fake.address(),
                nohp=fake.phone_number(),
            )

        for _ in range(10):
            BukuMasuk.objects.create(
                idbuku=Buku.objects.order_by('?').first(),  # Randomly select a Buku
                idpenerbit=Penerbit.objects.order_by('?').first(),  # Randomly select a Penerbit
                jumlah=fake.random_int(min=1, max=100)  # Random quantity between 1 and 100
             )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data.'))

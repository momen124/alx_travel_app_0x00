# listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Create or get a test user
        user, _ = User.objects.get_or_create(username='testuser', defaults={'password': 'password123'})
        
        # Clear existing listings
        Listing.objects.all().delete()

        # Seed 10 listings
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=random.uniform(50, 500),
                host=user
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with 10 listings'))
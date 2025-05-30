from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    host_username = serializers.ReadOnlyField(source='host.username')

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'host', 'host_username', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.ReadOnlyField(source='listing.title')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_title', 'user', 'user_username', 'start_date', 'end_date', 'total_price', 'created_at']
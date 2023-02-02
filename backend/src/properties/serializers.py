from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from src.properties.models import Property, PropertyViews


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    cover_photo = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()
    photo1 = serializers.SerializerMethodField()
    photo2 = serializers.SerializerMethodField()
    photo3 = serializers.SerializerMethodField()
    photo4 = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            "id",
            "user",
            "profile_photo",
            "title",
            "slug",
            "ref_code",
            "description",
            "country",
            "city",
            "postal_code",
            "street_address",
            "property_number",
            "price",
            "tax",
            "final_property_price",
            "plot_area",
            "total_floors",
            "bedrooms",
            "bathrooms",
            "advert_type",
            "property_type",
            "cover_photo",
            "published_status",
            "views",
        ]

    def get_user(self, obj):
        return obj.user.username

    def get_cover_photo(self, obj):
        return obj.cover_photo.url

    def get_profile_photo(self, obj):
        return obj.user.profile.profile_photo.url


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ["updated_at", "pkid"]


class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]

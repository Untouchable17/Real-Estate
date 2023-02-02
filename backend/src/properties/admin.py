from django.contrib import admin

from src.properties.models import Property, PropertyViews


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "country", 
        "advert_type", 
        "property_type"
    )
    list_filter = (
        "advert_type", 
        "property_type", 
        "country"
    )


admin.site.register(PropertyViews)

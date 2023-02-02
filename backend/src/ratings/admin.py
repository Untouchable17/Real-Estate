from django.contrib import admin

from src.ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("rater", "agent", "rating")



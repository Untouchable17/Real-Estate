from django.contrib import admin

from src.enquiries.models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "email", 
        "phone_number", 
        "message"
    )


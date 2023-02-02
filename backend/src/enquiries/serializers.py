from rest_framework import serializers

from src.enquiries.models import Enquiry


class EnquirySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enquiry
        fields = (
            "id",
            "name",
            "phone",
            "email",
            "subject",
            "message"
        )

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from src.enquiries.models import Enquiry
from src.enquiries.tasks import send_enquiry_email_task


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data
    try:
        send_enquiry_email.delay(data)
        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent. Please try again"})

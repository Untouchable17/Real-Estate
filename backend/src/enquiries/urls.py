from django.urls import path

from src.enquiries import views


urlpatterns = [
    path("", views.send_enquiry_email, name="enquiry_send"),
]

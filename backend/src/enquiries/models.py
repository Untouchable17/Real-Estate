from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from src.identify.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"),)
    phone_number = PhoneNumberField(
        max_length=30, 
        help_text="+7-928-...", 
        verbose_name= _("Phone number"),
    )
    email = models.EmailField(max_length=100, verbose_name=_("Email"))
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    message = models.TextField(max_length=5000, verbose_name=_("Message"))

    def __str__(self):
        return f"{self.email}"


    class Meta:
        verbose_name = "Enquirie"
        verbose_name_plural = "Enquiries"

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from phonenumber_field.modelfields import PhoneNumberField

from src.identify.models import TimeStampedUUIDModel


User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        max_length=30, help_text="+7-928-...", verbose_name=_("Phone Number"),
    )
    about_me = models.TextField(
        help_text="say something about yourself", verbose_name=_("About me"),
    )
    license = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_("Real Estate license"),
    )
    profile_photo = models.ImageField(
        default="/profile_default.png", verbose_name=_("Profile Photo")
    )
    gender = models.CharField(
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
        verbose_name=_("Gender"),
    )
    country = CountryField(
        blank=False, null=False, verbose_name=_("Country"),
    )
    city = models.CharField(
        max_length=180, blank=False, null=False, verbose_name=_("City"),
    )
    is_buyer = models.BooleanField(
        default=False,
        help_text=_("Are you looking to Buy a Property?"),
        verbose_name=_("Buyer"),
    )
    is_seller = models.BooleanField(
        default=False,
        help_text=_("Are you looking to sell a property?"),
        verbose_name=_("Seller"),
    )
    is_agent = models.BooleanField(
        default=False, help_text=_("Are you an agent?"), verbose_name=_("Agent"),
    )
    top_agent = models.BooleanField(default=False, verbose_name=_("Top Agent"))
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_("Number of Reviews"),
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

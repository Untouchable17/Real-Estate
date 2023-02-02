from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("src.profiles.urls")),
    path("api/v1/properties/", include("src.properties.urls")),
    path("api/v1/ratings/", include("src.ratings.urls")),
    path("api/v1/enquiries/", include("src.enquiries.urls")),
]


admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to the Real Estate Portal"

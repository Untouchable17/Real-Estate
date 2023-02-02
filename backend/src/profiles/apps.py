from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.profiles"

    def ready(self):
        from src.profiles import signals

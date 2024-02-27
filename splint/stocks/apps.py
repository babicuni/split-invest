from django.apps import AppConfig


class SpacesConfig(AppConfig):
    name = "splint.stocks"

    def ready(self):
        # Importing signals to ensure they're connected when the app starts
        from splint.stocks import signals  # noqa: F401

from django.apps import AppConfig


class PortalConfig(AppConfig):
    name = 'portal'

class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portal'

    def ready(self):
        import portal.signals

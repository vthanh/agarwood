from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'agarwood.apps'
    verbose_name = "Apps"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

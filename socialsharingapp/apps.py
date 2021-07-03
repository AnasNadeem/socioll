from django.apps import AppConfig


class SocialsharingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socialsharingapp'

    def ready(self):
        import socialsharingapp.signals
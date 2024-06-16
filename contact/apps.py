from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Provides primary key type for contact app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'

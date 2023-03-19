from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
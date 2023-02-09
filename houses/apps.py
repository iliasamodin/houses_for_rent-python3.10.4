from django.apps import AppConfig


class HousesConfig(AppConfig):                                                  # django class with application settings
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'houses'
    # class attribute responsible for the name of the application displayed in the administration panel
    verbose_name = 'Дома'

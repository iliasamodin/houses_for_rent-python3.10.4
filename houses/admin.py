from django.contrib import admin
from houses.models import House                                                              # import django model class


@admin.register(House)          # decorator linking the django admin panel class to the corresponding django model class
class HouseAdmin(admin.ModelAdmin):    # creating a django class to work with the model through the administration panel
    # class attribute responsible for the fields displayed for each model object in the admin panel
    list_display = ["name", "price", "active"]
    list_filter = ["active"]                                             # admin panel filter for records from sql table

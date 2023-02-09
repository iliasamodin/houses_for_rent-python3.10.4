from django.db import models


# django class for working with sql table
class House(models.Model):                                     # linking a python class to a framework using inheritance
    # creating a table column with type varchar via corresponding django class
    name = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")
    # django class ImageField passes links to images located in django project to sql table,
    #   the upload_to class attribute sets the path to the image relative to the media root folder,
    #   without taking into account the name of the image itself,
    #   default sets the name for the default image for each entry in the table,
    #   and blank true makes the field optional
    image = models.ImageField("Изображение", upload_to="houses/images", default="", blank=True)
    # logical column for records from the sql table, 
    #   responsible for displaying the object of the model class on the site
    active = models.BooleanField("Отображение на сайте", default=True)

    class Meta:             # the meta class inside the model is responsible for its basic settings and meta information
        # class attribute responsible for the name of the model displayed in the administration panel
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        # class attribute responsible for sorting model objects in the admin panel and website
        ordering = ["-active", "name"]  

    # changing the names displayed on the site for objects of the model class to the value of their attribute
    def __str__(self):
        return self.name

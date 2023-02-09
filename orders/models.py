from django.db import models
from houses.models import House                                                   # import model from another django app


class Order(models.Model):
    # the on_delete foreign key class constructor argument with the value models.SET_NULL
    #   will create a task to automatically delete records in the current table
    #   when related records in the foreign table are deleted
    house = models.ForeignKey(House, verbose_name="Дом", null=True, on_delete=models.SET_NULL)
    client_name = models.CharField("Имя", max_length=50)
    client_phone = models.CharField("Телефон", max_length=20)
    # the constructor argument of the date and time class auto_now_add with a value of true
    #   will automatically insert the current date and time into the column at the time the record was added
    application_date = models.DateTimeField("Дата подачи заявки", auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["application_date"]

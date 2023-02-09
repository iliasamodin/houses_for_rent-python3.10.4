from django import forms
from orders.models import Order
from houses.models import House


class OrderForm(forms.ModelForm):                                 # class for generating html form based on django model
    # manual setting of characteristics for one of the django form fields:
    #   selection from all sql records of the "house" table, the format of the field is hidden
    house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.HiddenInput)
    # checkbox without filling which you can not send an application
    personal_data = forms.BooleanField(label="Я даю согласие на обработку моих персональных данных", required=True)

    class Meta:
        model = Order                # designation of the table in which the data from the completed form will be placed
        fields = ["house", "client_name", "client_phone"]       # enumeration of fields to fill displayed for the client

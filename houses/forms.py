from django import forms


class HouseFilterForm(forms.Form):                                              # django form to filter data on the page
    # form fields for filtering objects displayed on the page
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    # the CharField filter field is used to search for content inside the text fields of the model class object
    query = forms.CharField(label="описание", required=False)
    # filter form field with preset options
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
            # tuples are variants of the form field, the first elements of the tuples are for django, 
            #   the second for displaying to users
            ("name", "по алфавиту"),
            ("price", "по увеличению цены"),
            # the minus sign at the beginning of the first element of the tuple 
            #   is responsible for sorting in reverse order
            ("-price", "по уменьшению цены")
        ]
    )
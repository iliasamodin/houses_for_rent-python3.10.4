from django.shortcuts import render
# function import to get specific class model object from sql table
from django.shortcuts import get_object_or_404
# importing a function to redirect the user to another page after submitting the form
from django.http import HttpResponseRedirect
from django.urls import reverse                                 # import of a function similar to the "url" template tag
# the class name is short for query, he allows you to create complex filters using the or operator
from django.db.models import Q
from houses.models import House                                       # import table-model to get records from sql table
from orders.forms import OrderForm                                                                  # django form import
from houses.forms import HouseFilterForm


# view function for the main page of the site,
#   which receives the user's request as an argument, and returns the html page
def houses_list(request):
    # creating the basis of the request to receive records from the model table, 
    #   later filters will be added to the basis of the template, 
    #   the request itself will be sent only at the time of rendering the page
    #   (extraction occurs using orm sql query)
    houses = House.objects.filter(active=True)             # queryset - a set of django data retrieved using a SQL query
    # so that the form is not cleared when submitting data, 
    #   you must pass the request parameter to it, with the value get
    form = HouseFilterForm(request.GET)
    if form.is_valid():
        # a condition that checks which form fields were filled in and submitted by the get request
        if form.cleaned_data["min_price"]:
            # the filter filters the records from the sql table 
            #   receiving when rendering the page in accordance with the condition
            #   (in this case, the value of the price field for the table record must be greater than 
            #   or equal to what the user entered in the min_price field)
            houses = houses.filter(price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            houses = houses.filter(price__lte=form.cleaned_data["max_price"])
        if form.cleaned_data["query"]:
            # the filtering suffix __icontains, for a text field, 
            #   indicates that the text field content must contain the text declared to the right of the equal sign, 
            #   case insensitive
            houses = houses.filter(
                # placing multiple filter conditions, in the Q class, with a separator between them, 
                #   adds a condition with an "or" operator between the multiple conditions in brackets 
                #   relative to the other "and" conditions, if any
                Q(description__icontains=form.cleaned_data["query"]) |
                Q(name__icontains=form.cleaned_data["query"])
            )
        if form.cleaned_data["ordering"]:
                # the order_by method is responsible for sorting the records in the django query to the sql table 
                #   sent when the page is rendered
            houses = houses.order_by(form.cleaned_data["ordering"])

    # if the user's request does not involve any page modifications,
    #   then the render function will return the html page in its original format
    return render(request, "houses/houses_list.html", 
        # dictionary transfers the list and the form to html file
        {
            "houses": houses[:12],      # the number of model class objects passed to the page can be limited by a slice
            "form": form
        }
    )


# the function of representing a specific object of the model class
#   as the second argument receives the identifier of this object
def house_details(request, house_id):
    # assigning a specific model class object to the house variable by its identifier,
    #   or displaying a 404 page if there is no object with such an identifier in the sql table
    #   (or displaying a 404 page if the status of the found object is active=false)
    house = get_object_or_404(House, id=house_id, active=True)
    # passing data from a post request to django if the form has been submitted
    #   (the form field house is automatically filled with the house that is open on the page)
    form = OrderForm(request.POST or None, initial={"house": house})               # putting django form into a variable
    # save the data of the completed form to the database,
    #   provided that the sending method is post, and the form itself is valid
    if request.method == "POST" and form.is_valid():
        form.save()
        # like the url template tag, the reverse function takes the page name from urlpatterns
        #   and additional parameters to pass to the page view
        url = reverse("house", kwargs={"house_id": house.id})
        # after the form is saved, the HttpResponseRedirect and reverse functions refresh the current page for the user
        #   and clear the form
        return HttpResponseRedirect(f"{url}?send=1")

    # the dictionary element with the form key will pass the django form to the html template
    return render(request, "houses/house_details.html",
        {
            "house": house,
            "form": form,
            # passing to the template a boolean value
            #   associated with the presence or absence of send in the list of parameters received by get
            "send": request.GET.get("send")
        }
    )


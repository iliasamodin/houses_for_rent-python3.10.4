"""houses_for_rent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static              # import of the function responsible for processing static files
from django.conf import settings                  # import project settings to access addresses and paths of media files
from houses.views import houses_list                                            # import a page view to a file with urls
from houses.views import house_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # name attribute for the path function is responsible for the name of the page
    path('', houses_list, name='main'),           # placing the homepage view function in the site's internal links list
    # placing a page view function for a specific model object in the site's internal links list
    path('<int:house_id>', house_details, name='house')         # <int:house_id> points to the id in the url of the page
]

# adding a media_url link to media_root for static files to the site's internal links list
urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

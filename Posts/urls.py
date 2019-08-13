from django.urls import path

from .views import home_page#, about_page, contact_page


urlpatterns = [
    path('', home_page),
]
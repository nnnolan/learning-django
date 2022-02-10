from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
# makes the urls.py file available to the rest of the application
# the urls.py file is the main entry point for the application

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # A simple view for the index page
]

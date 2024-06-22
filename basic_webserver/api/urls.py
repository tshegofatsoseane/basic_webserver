from django.urls import path
from . import views

urlpatterns = [
    path('visitor', views.greet_visitor, name='greet_visitor'),  
]

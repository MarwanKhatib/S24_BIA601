from django.urls import path
from . import views

urlpatterns = [
    path('', views.run_genetic_algorithm, name='run_genetic_algorithm'),  # Define the root path
]

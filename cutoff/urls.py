from django.urls import path
from . import views

urlpatterns = [
    path("", views.calculator, name="calculator"),
    path("history/", views.history, name="history"),
]
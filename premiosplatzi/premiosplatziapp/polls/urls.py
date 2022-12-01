from django.urls import admin

from . import views

urlpatterns = [
    path("", views.index, name="index")
]

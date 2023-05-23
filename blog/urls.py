from django.urls import path
from . import views

urlpatterns = [
    path(r"^$", views.post, name="hw10")
]
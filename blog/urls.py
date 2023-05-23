from django.urls import path
from . import views

urlpatterns = [
    path(f"^$", views.post_list, name="post_list")
]
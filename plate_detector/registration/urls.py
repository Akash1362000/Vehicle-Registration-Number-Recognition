from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.upload_image, name="upload_image"),
    path("", views.image_list, name="image_list"),
]

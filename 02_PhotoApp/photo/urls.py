from django.urls import path

from photo import views

urlpatterns = [path("", views.photo_list, name="photo_list")]

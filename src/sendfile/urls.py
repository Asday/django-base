from django.urls import path

from . import views


urlpatterns = [
    path("private/", views.PrivateFile.as_view()),
]

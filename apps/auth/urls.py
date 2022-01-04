from django.urls import path

from .views import test_view

app_name = "auth"

urlpatterns = [
    path("", test_view, name="test"),
]

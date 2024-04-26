from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "findatherapist"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", views.index, name="index"),
]

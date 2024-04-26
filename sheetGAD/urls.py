from django.contrib import admin
from django.db import router
from django.urls import include, path

from . import views
from .views import GADView

app_name = "sheetGAD"

urlpatterns = [
    path("GAD/", GADView.as_view(), name="GAD"),
]

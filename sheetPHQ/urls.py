from django.contrib import admin
from django.db import router
from django.urls import path, include

from . import views
from .views import PHQView


app_name = 'sheetPHQ'

urlpatterns = [

    path('PHQ/', PHQView.as_view(),
         name="PHQ"),
]

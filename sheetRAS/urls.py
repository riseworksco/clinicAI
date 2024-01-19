from django.contrib import admin
from django.db import router
from django.urls import path, include

from . import views
from .views import RASView


app_name = 'sheetRAS'

urlpatterns = [

    path('RAS/', RASView.as_view(),
         name="RAS"),
]

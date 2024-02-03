from django.contrib import admin
from django.db import router
from django.urls import path, include

from . import views
from .views import CAMView


app_name = 'sheetCAM1'

urlpatterns = [

    path('sheetCAM1/', CAMView.as_view(),
         name="CAM1"),
]

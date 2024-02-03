from django.contrib import admin
from django.db import router
from django.urls import path, include

from . import views
from .views import AAQIIView


app_name = 'sheetAAQII'

urlpatterns = [

    path('AAQII/', AAQIIView.as_view(),
         name="AAQII"),
]

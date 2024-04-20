from django.contrib import admin
from django.db import router
from django.urls import include, path

from . import views
from .views import AT4View

app_name = 'sheet4AT'

urlpatterns = [

    path('sheet4AT/', AT4View.as_view(),
         name="sheet4AT"),
]

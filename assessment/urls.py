"""Music_Therapy_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include

from . import views
from .views import StompView, StompSuccessView

# import patient_management
app_name = 'assessment'

urlpatterns = [
    # path('stomp/', views.stomp, name='stomp'),
    path('stomp/', StompView.as_view(), name="contact"),
    path('success/', StompSuccessView.as_view(), name="success"),
    path('neurologic_screening_evaluation/', views.neurologic_screening_evaluation,
         name="Neurologic_Screening_Evaluation"),
    path('pre_post_tests/', views.pre_post_form,
         name="pre_post_tests/")
]

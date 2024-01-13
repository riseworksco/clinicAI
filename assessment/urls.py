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
from .views import StompView, StompSuccessView, PsychoemotionalScreeningEvaluationView, PrePostView, \
    NeurologicScreeningEvaluationView

# import patient_management
app_name = 'assessment'

urlpatterns = [
    # path('stomp/', views.stomp, name='stomp'),
    path('', views.index, name='index'),
    path('stomp/', StompView.as_view(), name="stomp"),
    path('success/', StompSuccessView.as_view(), name="success"),
    path('neurologic_screening_evaluation/', NeurologicScreeningEvaluationView.as_view(),
         name="Neurologic_Screening_Evaluation"),
    path('pre_post_tests/', PrePostView.as_view(),
         name="pre_post_tests"),
    path('Psychoemotional_Screening_Evaluation/', PsychoemotionalScreeningEvaluationView.as_view(),
         name="Psychoemotional_Screening_Evaluation"),
    path('pdf/',views.some_view,name='pdf'),
    path('pdf/',views.all_view,name='all')
]

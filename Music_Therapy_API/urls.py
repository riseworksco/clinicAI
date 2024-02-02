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

# import patient_management

urlpatterns = [
    path('', include('app.urls')),
    path('email/', include('email_service.urls')),
    path('admin/', admin.site.urls),
    path('patient/', include('patient_management.urls')),
    path('music/', include('music_management.urls')),
    path('chat/', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
    path('assessment/', include('assessment.urls')),
    path('sheetRAS/', include('sheetRAS.urls')),
    path('sheet4AT/', include('sheet4AT.urls')),
    # path('sheetCAM/', include('sheetCAM.urls')),
    path('sheetCAM1/', include('sheetCAM1.urls')),

]

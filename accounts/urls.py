from django.urls import include, path

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.display_profile, name="profile")
]

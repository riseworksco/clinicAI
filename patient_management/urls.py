from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", views.display_patients, name="index"),
    re_path(
        r"^view_patient/(?P<patient_username>[-\w]+)$",
        views.display_patient,
        name="view_patient",
    ),
    path("api/", include(router.urls)),
    path("sessions", views.display_sessions, name="sessions"),
    re_path(
        r"^session/(?P<session_id>[-\w]+)$",
        views.display_session,
        name="session",
    ),
]

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'playlists', views.PlaylistViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index, name='index'),
    path('songs/', views.display_songs, name="songs"),
]

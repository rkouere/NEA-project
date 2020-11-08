from django.urls import include, path
from rest_framework import routers
from . import views
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'bird', views.BirdViewSet)
router.register(r'result', views.ResultsViewSet)
router.register(r'networks', views.NetworksViewSet)
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
]
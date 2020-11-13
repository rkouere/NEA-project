# from my online research, this file only run once, so the startup code is here

from django.urls import include, path
from rest_framework import routers
from . import views
from .views import UploadViewSet
from .predict import load_networks

router = routers.DefaultRouter()
router.register(r'bird', views.BirdViewSet)
router.register(r'result', views.ResultsViewSet)
router.register(r'networks', views.NetworksViewSet)
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
]

def startup():
    load_networks()
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import UploadViewSet

# Creates all the urls for the API
router = routers.DefaultRouter()
router.register(r'bird', views.BirdViewSet)
router.register(r'result', views.ResultsViewSet)
router.register(r'network', views.NetworkViewSet)
router.register(r'accuracy', views.GetAccuracyRate, basename="accuracy")
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    # url(r'^api/bird$', views.bird_list),
    # url(r'^api/bird/(?P<pk>[0-9]+)$', views.bird_detail)
]

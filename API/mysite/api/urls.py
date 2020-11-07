from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'birds', views.BirdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^', include('bird.urls')),

    # path(r'bird/(?<pk>[0-9]+)', views.bird_detail)
    # path(r'bird/id', views.bird_list_id)

    path(r'bird', views.bird_list),
    url(r'^bird/(?P<pk>[0-9]+)$', views.bird_detail),

    path(r'results', views.results_list),
    url(r'^results/(?P<pk>[0-9]+)$', views.results_detail),

    path(r'networks', views.networks_list),
    url(r'^networks/(?P<pk>[0-9]+)$', views.networks_detail),
]

# notes

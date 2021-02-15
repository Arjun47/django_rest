from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ghar', views.GharViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.urls import path, include

from rest_framework import routers

from apps.rate.views import RateViewSet


router = routers.DefaultRouter()
router.register('', RateViewSet)

urlpatterns = [
    path('', include(router.urls))
]

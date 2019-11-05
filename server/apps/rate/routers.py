from rest_framework import routers

from apps.rate.viewsets import RateViewSet

rates_router = routers.DefaultRouter()
rates_router.register('rates', RateViewSet)

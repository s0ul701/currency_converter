from apps.rate.viewsets import RateViewSet

from rest_framework import routers


rates_router = routers.DefaultRouter()
rates_router.register('rates', RateViewSet)

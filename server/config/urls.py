from django.contrib import admin
from django.urls import include, path

from apps.rate.routers import rates_router

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rates_router.urls))
]

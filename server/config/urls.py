from server.apps.rate.routers import rates_router

from django.contrib import admin
from django.urls import path, include


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rates_router.urls))
]

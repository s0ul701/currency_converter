from django.contrib import admin
from django.urls import path, include


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rates/', include('apps.rate.urls'))
]

from django.contrib import admin

from djmoney.contrib.exchange import models

from .models import Rate


# Unregister Rate model from djmoney library
admin.site.unregister(models.Rate)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    """Admin panel for displaying Rate model"""
    readonly_fields = (
        'from_cur',
        'to_cur',
        'rate',
        'updated_at'
    )

    list_filter = ('from_cur', 'to_cur')

    def has_add_permission(self, request):
        """Forbid manually adding of Rate instances"""
        return False

from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.rate.models import Rate
from apps.rate.serializers import RateSerializer


class RateViewSet(ReadOnlyModelViewSet):
    """Class for providing API for Rate model"""
    serializer_class = RateSerializer
    # queryset = Rate.objects.all()

    def get_queryset(self):
        rates = Rate.objects.filter(rate__isnull=False)
        from_cur = self.request.query_params.get('from_cur', None)
        to_cur = self.request.query_params.get('to_cur', None)

        if from_cur:
            rates = rates.filter(from_cur=from_cur)
        if to_cur:
            rates = rates.filter(to_cur=to_cur)

        return rates

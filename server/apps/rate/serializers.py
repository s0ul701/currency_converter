from rest_framework.serializers import ModelSerializer

from apps.rate.models import Rate


class RateSerializer(ModelSerializer):
    """Serializer for Rate model"""
    class Meta:
        model = Rate
        fields = ('from_cur', 'to_cur', 'rate', 'updated_at')

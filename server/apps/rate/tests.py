from rest_framework.test import APITestCase

from apps.rate.models import Rate, CURRENCY_CHOICE
from apps.rate.serializers import RateSerializer


class RateAPITestCase(APITestCase):
    """Test class for Rates app"""

    def test_get_all_initial_rates(self):
        """Test if initial data migration for rates creates all rates"""
        for (from_cur, _) in CURRENCY_CHOICE:
            for (to_cur, _) in CURRENCY_CHOICE:
                if from_cur != to_cur:
                    self.assertEqual(
                        Rate.objects.filter(from_cur=from_cur, to_cur=to_cur).count(),
                        1
                    )

    def test_get_all_rates(self):
        """Test if server returns all existing values"""
        response = self.client.get('/rates/')
        self.assertEqual(response.status_code, 200)

        response_serializer = RateSerializer(data=response.data)
        response_serializer.is_valid()
        rates = Rate.objects.all()
        self.assertEqual(
            response_serializer.initial_data,
            RateSerializer(rates, many=True).data
        )

from apps.rate.models import Rate, Currencies
from apps.rate.serializers import RateSerializer
from apps.rate.tasks import update_rates

from django.test import TestCase

from rest_framework.test import APITestCase


class RateAPITestCase(APITestCase):
    """Test class for Rates app"""

    def test_get_all_initial_rates(self):
        """Test if initial data migration for rates creates all rates"""
        for from_cur, _ in Currencies.CHOICES:
            for to_cur, _ in Currencies.CHOICES:
                if from_cur != to_cur:
                    self.assertEqual(
                        Rate.objects.filter(from_cur=from_cur, to_cur=to_cur).count(),
                        1
                    )

    def test_get_all_rates(self):
        """Test if server returns all existing values"""
        response = self.client.get('/api/rates/')
        self.assertEqual(response.status_code, 200)

        response_serializer = RateSerializer(data=response.data)
        response_serializer.is_valid()
        rates = Rate.objects.all()
        self.assertEqual(
            response_serializer.initial_data,
            RateSerializer(rates, many=True).data
        )


class RatesTaksTestCase(TestCase):
    """Class for testing Rate`s app tasks"""
    def test_rates_update_task(self):
        """Test if rates before update and after update have different date modification"""
        last_update_dates = {
            rate.id: rate.updated_at
            for rate in Rate.objects.only('id', 'updated_at')}
        update_rates()
        for (rate_id, rate_update) in last_update_dates.items():
            self.assertNotEqual(
                Rate.objects.get(id=rate_id).updated_at,
                rate_update
            )
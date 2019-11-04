from celery import shared_task
from djmoney.contrib.exchange.backends import OpenExchangeRatesBackend
from djmoney.contrib.exchange.models import get_rate

from apps.rate.models import Rate
from config.settings import OPEN_EXCHANGE_RATES_URL


@shared_task
def update_rates():
    backend = OpenExchangeRatesBackend(url=OPEN_EXCHANGE_RATES_URL)
    backend.update_rates()

    for rate in Rate.objects.all():
        rate.rate = get_rate(rate.from_cur, rate.to_cur, backend=backend.name)
        rate.save(update_fields=('rate', 'updated_at',))

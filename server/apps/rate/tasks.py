from celery import task
from django.db.utils import ProgrammingError
from djmoney.contrib.exchange.backends import OpenExchangeRatesBackend
from djmoney.contrib.exchange.models import get_rate
from urllib.error import URLError

from apps.rate.models import Rate
from config.settings import OPEN_EXCHANGE_RATES_URL


@task()
def update_rates():
    backend = OpenExchangeRatesBackend(url=OPEN_EXCHANGE_RATES_URL)
    try:
        backend.update_rates()

        for rate in Rate.objects.all():
            rate.rate = get_rate(rate.from_cur, rate.to_cur, backend=backend.name)
            rate.save(update_fields=('rate', 'updated_at',))
    except URLError:
        for rate in Rate.objects.all():
            rate.save(update_fields=(('updated_at',)))
    except ProgrammingError:
        pass

# Generated by Django 2.2.6 on 2019-10-30 08:36

from django.db import migrations
from djmoney.contrib.exchange.backends import OpenExchangeRatesBackend
from djmoney.contrib.exchange.models import get_rate

from apps.rate.models import CURRENCY_CHOICE, Rate
from config.settings import OPEN_EXCHANGE_RATES_URL


def load_init_rates(*args, **kwargs):
    """Loads inintial rates of currencies"""
    backend = OpenExchangeRatesBackend(url=OPEN_EXCHANGE_RATES_URL)
    backend.update_rates()

    currencies = [currency for (currency, _) in CURRENCY_CHOICE]
    for currency1 in currencies:
        for currency2 in currencies:
            if currency1 != currency2:
                Rate.objects.create(
                    from_cur=currency1,
                    to_cur=currency2,
                    rate=get_rate(currency1, currency2, backend=backend.name)
                )


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_init_rates)
    ]

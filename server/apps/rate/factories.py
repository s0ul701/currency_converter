import factory
from factory.fuzzy import FuzzyDecimal, FuzzyChoice

from apps.rate.models import Rate, CURRENCY_CHOICE


class RateFactory(factory.DjangoModelFactory):
    class Meta:
        model = Rate

    from_cur = FuzzyChoice([currency[0] for currency in CURRENCY_CHOICE])
    to_cur = FuzzyChoice([currency[0] for currency in CURRENCY_CHOICE])
    rate = FuzzyDecimal(0, 1000000, 12)

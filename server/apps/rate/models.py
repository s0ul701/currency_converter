from django.db import models


class Currencies:
    CZK = 'CZK'
    EUR = 'EUR'
    PLN = 'PLN'
    USD = 'USD'

    CURRENCIES = (
        CZK,
        EUR,
        PLN,
        USD,
    )

    CHOICES = (
        (CZK, 'Czech Republic Koruna'),
        (EUR, 'Euro'),
        (PLN, 'Polish Zloty'),
        (USD, 'United States Dollar')
    )


class Rate(models.Model):
    """Model for storing rate of currencies

    Fields:
        from_cur (str): input currency for conversation
        to_cur (str): result currency for conversation
        rate (float): current rate of `from_cur` currency
            relatively to `to_cur`
        updated_at (datetime): date and time of last rate update
    """
    from_cur = models.CharField(
        max_length=3,
        verbose_name='Currency for conversation',
        choices=Currencies.CHOICES
    )

    to_cur = models.CharField(
        max_length=3,
        verbose_name='Result currency',
        choices=Currencies.CHOICES
    )

    rate = models.DecimalField(
        max_digits=19,
        decimal_places=12,
        verbose_name='Current rate',
        null=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Last update'
    )

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self):
        return f'{self.from_cur} -> {self.to_cur} = {self.rate} ({self.updated_at})'

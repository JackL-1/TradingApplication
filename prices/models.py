from django.db import models
from assets.models import Asset 
from decimal import Decimal


class Price(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00'))
    open_price = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00'))
    close_price = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00'))
    low_price = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00'))
    high_price = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00'))
    previous_close = models.DecimalField(max_digits=20, decimal_places=5, default=Decimal('0.00'))
    change =models.DecimalField(max_digits=7, decimal_places=5,  default=Decimal('0.00'))
    percent_change = models.DecimalField(max_digits=7, decimal_places=5, default=Decimal('0.00'))




from django.db import models

# Create your models here.
from prices.models import Price
from assets.models import Asset
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

class Trade(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    execution_timestamp = models.DateTimeField()
    quantity = models.FloatField(validators=[MinValueValidator(0.1)], default=0.00)
    BUY = 'BUY'
    SELL = 'SELL'
    TRADE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]
    buy_sell = models.CharField(max_length=4, choices=TRADE_CHOICES)
    
    def execution_price(self):
        latest_price = Price.objects.filter(
            asset=self.asset, timestamp__lte=self.execution_timestamp
        ).order_by('-timestamp').first()
        if latest_price:
            return latest_price.price
        return None

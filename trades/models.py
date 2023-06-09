from django.db import models

# Create your models here.
from prices.models import Price
from assets.models import Asset
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
from decimal import Decimal

class Trade(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    execution_timestamp = models.DateTimeField()
    quantity = models.DecimalField(validators=[MinValueValidator(0.1), MaxValueValidator(1000)],decimal_places=2,max_digits=6, default=0.00)
    execution_price = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00'))
    BUY = 'BUY'
    SELL = 'SELL'
    TRADE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
    ]
    buy_sell = models.CharField(max_length=4, choices=TRADE_CHOICES)

    def get_latest_price(self):
        # Get the latest price for the asset
        latest_price = Price.objects.filter(asset_id=self.asset_id).order_by('-timestamp').first()
        if latest_price:
            return latest_price.price
        return None
    
    @property
    def pnl(self):
        current_price = self.get_latest_price()
        print('current_price', current_price)
        execution_price = self.execution_price

        if abs(current_price == execution_price):
            print(f'Calc HIT for: current = execution: Trade ID: {self.id}, Buy/Sell : {self.buy_sell}, PnL: {Decimal("0.000")}')
            return Decimal('0.000')

        if self.buy_sell == Trade.BUY:
            if current_price > execution_price:
                pnl_value = abs((current_price - execution_price) * Decimal(str(self.quantity)))
                print ('BUY calc HIT for: current>execution', 'RESULT:', pnl_value)
            else:
                pnl_value = abs((execution_price - current_price) * Decimal(str(self.quantity)))
                print ('BUY calc HIT for: current<execution', pnl_value)
        else:  # self.buy_sell == Trade.SELL
            if current_price < execution_price:
                pnl_value = abs((execution_price - current_price) * Decimal(str(self.quantity)))
                print ('SELL calc HIT for: current<execution', pnl_value)
            else:
                pnl_value = -abs((current_price - execution_price) * Decimal(str(self.quantity)))
                print ('SELL calc HIT for: current>execution', pnl_value)

        print(f'Trade ID: {self.id}, Buy/Sell : {self.buy_sell},EXECUTION PRICE:{ self.execution_price}  PnL: {pnl_value}')
        return pnl_value

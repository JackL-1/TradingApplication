from django.db.models.signals import post_save
from django.dispatch import receiver
from prices.models import Price
from trades.models import Trade

@receiver(post_save, sender=Price)
def recalculate_pnl(sender, instance, **kwargs):
    print("---------------Receiver signal hit---------------")
    trades = Trade.objects.filter(asset_id=instance.asset_id)
    for trade in trades:
        # Access the pnl property to calculate the PnL for each trade
        pnl = trade.pnl




from django.apps import AppConfig
from django.db.models.signals import post_save
from django.apps import apps

class TradesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trades'

    def ready(self):
        from . import signals  # Import signals.py
        from prices.models import Price
        post_save.connect(signals.recalculate_pnl, sender=Price)  # Connect the signal

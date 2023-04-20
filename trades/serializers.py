from rest_framework import serializers
from .models import Trade
from prices.models import Price
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from django.utils import timezone


class TradeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    execution_timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    pnl = serializers.SerializerMethodField()
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Trade
        fields = ('id', 'user_id', 'asset', 'quantity', 'buy_sell', 'execution_timestamp', 'execution_price', 'pnl')

    def get_pnl(self, obj):
        return obj.pnl



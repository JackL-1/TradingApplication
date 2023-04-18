from rest_framework import serializers
from .models import Trade
from prices.models import Price


class TradeSerializer(serializers.ModelSerializer):
    asset_name = serializers.CharField(source='asset.name')
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.username')
    execution_timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    pnl = serializers.SerializerMethodField()

    class Meta:
        model = Trade
        fields = ['id', 'asset', 'asset_name', 'user_id', 'user_name',
                  'execution_timestamp', 'volume', 'buy_sell', 'pnl']

    def get_pnl(self, obj):
        latest_price = Price.objects.filter(
            asset=obj.asset, timestamp__lte=obj.execution_timestamp
        ).order_by('-timestamp').first()
        if latest_price:
            current_price = latest_price.price
            execution_price = obj.execution_price()
            if execution_price:
                pnl_calculation = {
                    Trade.BUY: round((current_price - execution_price) * obj.volume, 2),
                    Trade.SELL: round(
                        (execution_price - current_price) * obj.volume, 2)
                }
                return pnl_calculation.get(obj.buy_sell, None)
        return None

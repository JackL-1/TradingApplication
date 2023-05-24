from rest_framework import serializers
from ..models import Trade
from assets.models import Asset

class TradeSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    execution_timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    pnl = serializers.SerializerMethodField()
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    ticker = serializers.PrimaryKeyRelatedField(queryset=Asset.objects.all(), source='asset.ticker')

    class Meta:
        model = Trade
        fields = '__all__'

    def get_pnl(self, obj):
        return obj.pnl



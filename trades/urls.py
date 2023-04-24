from django.urls import path
from .views import TradePostView, TradePreConfirm, ExitTradeView, TradesView

urlpatterns = [
    path('trade/', TradePostView.as_view(), name='trade_post'),
    path('trades/', TradesView.as_view(), name='trades'),
    path('pre_confirm/', TradePreConfirm.as_view(), name='trade_preconfirm'),
    path('takeprofit/<int:trade_id>/', ExitTradeView.as_view(), name='exit_trade'),
]


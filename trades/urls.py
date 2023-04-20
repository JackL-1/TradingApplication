from django.urls import path
from .views import TradePostView, ExitTradeView

urlpatterns = [
    path('', TradePostView.as_view(), name='trade_post'),
    path('takeprofit/<int:trade_id>/', ExitTradeView.as_view(), name='exit_trade'),
]


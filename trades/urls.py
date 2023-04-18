from django.urls import path
from .views import TradePostView

urlpatterns = [
  path('', TradePostView.as_view())
]

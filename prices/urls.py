from django.urls import path
from .views import GetAllPricesView, GetSinglePriceView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('fetch-prices/', csrf_exempt(GetAllPricesView.as_view())),
    path('fetch-price/', csrf_exempt(GetSinglePriceView.as_view())),
]
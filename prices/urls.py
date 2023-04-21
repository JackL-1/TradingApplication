from django.urls import path
from .views import GetPriceView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('fetch-price/', csrf_exempt(GetPriceView.as_view())),
]
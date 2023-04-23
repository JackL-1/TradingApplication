from django.urls import path
from .views import GetAllAssetsView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('assets/', csrf_exempt(GetAllAssetsView.as_view())),
]
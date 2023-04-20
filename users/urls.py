from django.urls import path
from .views import RegisterView, LoginView, AddFundsForm

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('add_funds/', AddFundsForm.as_view(),),
]
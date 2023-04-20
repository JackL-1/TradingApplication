from django.urls import path
from .views import RegisterView, LoginView, AddFunds, RemoveFunds 

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('add_funds', AddFunds.as_view()), 
    path('remove_funds', RemoveFunds.as_view()),  
]

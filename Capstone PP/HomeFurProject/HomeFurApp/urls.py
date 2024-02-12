from .views import LoginView, RegisterView, AlldataView
from django.urls import path 





urlpatterns = [
    path('data', AlldataView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view())
]


from django.urls import path
from .views import RegisterView,home, LoginView,IsAuthenticated

urlpatterns = [
    path('', home, name='home'), 
    # path('', IsAuthenticated.as),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login')
]

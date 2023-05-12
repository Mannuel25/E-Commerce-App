from django.urls import path, include
from .views import HomePageView, DashboardPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
]

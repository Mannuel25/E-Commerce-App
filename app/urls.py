# from .views import HomePageView, DashboardView, add_clothings, all_clothings,  clothings_detail, delete_clothings, edit_clothings
from .views import HomePageView, DashboardPageView, all_clothings
from django.urls import path, include


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('clothings/', all_clothings, name='clothings'),
    # path('clothings/create', add_clothings, name='add_clothings'),
    # path('clothings/view/<int:id>', clothings_detail, name='clothings_detail'),
    # path('clothings/edit/<int:id>', edit_clothings, name='edit_clothings'),
    # path('clothings/delete/<int:id>', delete_clothings, name='delete_clothings'),

]

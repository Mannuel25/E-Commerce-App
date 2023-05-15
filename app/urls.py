# from .views import HomePageView, DashboardView, add_clothings, all_clothings,  clothings_detail, delete_clothings, edit_clothings
from .views import HomePageView, DashboardPageView, all_clothings, add_products, cart, phones_accessories
from django.urls import path, include


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('phones_accessories/', phones_accessories, name='phones_accessories'),
    path('cart/', cart, name='cart'),
    path('clothings/', all_clothings, name='clothings'),
    path('products/create', add_products, name='add_products'),
    # path('clothings/view/<int:id>', clothings_detail, name='clothings_detail'),
    # path('clothings/edit/<int:id>', edit_clothings, name='edit_clothings'),
    # path('clothings/delete/<int:id>', delete_clothings, name='delete_clothings'),

]

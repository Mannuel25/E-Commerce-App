# from .views import HomePageView, DashboardView, add_clothings, all_clothings,  clothings_detail, delete_clothings, edit_clothings
from .views import HomePageView, DashboardPageView, all_clothings, add_products, cart, phones_accessories, edit_phones
from django.urls import path, include


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('phones_accessories/', phones_accessories, name='phones_accessories'),
    path('cart/', cart, name='cart'),
    path('clothings/', all_clothings, name='clothings'),
    path('products/create', add_products, name='add_products'),
    # path('clothings/view/<int:id>', clothings_detail, name='clothings_detail'),
    path('phones_accessories/edit/<int:id>', edit_phones, name='edit_phones'),
    # path('clothings/delete/<int:id>', delete_clothings, name='delete_clothings'),

]

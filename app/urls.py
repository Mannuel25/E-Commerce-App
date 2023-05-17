from .views import HomePageView, DashboardPageView, all_clothings, add_products, cart, phones_accessories, edit_phones, edit_clothings, gaming, edit_game_products, health_beauty, edit_health_beauty, home_office, edit_home_office
from django.urls import path, include


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('cart/', cart, name='cart'),
    path('clothings/', all_clothings, name='clothings'),
    path('clothings/edit/<int:id>', edit_clothings, name='edit_clothings'),
    path('products/create', add_products, name='add_products'),
    path('phones_accessories/', phones_accessories, name='phones_accessories'),
    path('phones_accessories/edit/<int:id>', edit_phones, name='edit_phones'),
    path('gaming/', gaming, name='gaming'),
    path('gaming/edit/<int:id>', edit_game_products, name='edit_game_products'),
    path('health_beauty/', health_beauty, name='health_beauty'),
    path('health_beauty/edit/<int:id>', edit_health_beauty, name='edit_health_beauty'),
    path('home_office/', home_office, name='home_office'),
    path('home_office/edit/<int:id>', edit_home_office, name='edit_home_office'),

]

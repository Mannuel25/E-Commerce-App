from django.urls import path, include
from .views import signin, signout, signup

urlpatterns = [
    path('login/', signin, name='login'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='logout'),
]

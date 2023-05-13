from django import forms
from .models import Clothings, PhoneAndAccessories, HomeAndOffice, HealthAndBeauty, Gaming


class ClothingsForm(UserChangeForm):
    class Meta:
        fields = '__all__'
        model = Clothings

class PhoneAndAccessoriesForm(UserChangeForm):
    class Meta:
        fields = '__all__'
        model = PhoneAndAccessories


class HomeAndOfficeForm(UserChangeForm):
    class Meta:
        fields = '__all__'
        model = HomeAndOffice

class HealthAndBeautyForm(UserChangeForm):
    class Meta:
        fields = '__all__'
        model = HealthAndBeauty


class GamingForm(UserChangeForm):
    class Meta:
        fields = '__all__'
        model = Gaming

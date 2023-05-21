from django import forms
from .models import Clothings, PhoneAndAccessories, HomeAndOffice, HealthAndBeauty, Gaming, Cart, AllProducts


class ClothingsForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Clothings


class PhoneAndAccessoriesForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = PhoneAndAccessories


class HomeAndOfficeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = HomeAndOffice


class HealthAndBeautyForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = HealthAndBeauty


class GamingForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Gaming


class CartForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Cart


class AllProductsForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = AllProducts

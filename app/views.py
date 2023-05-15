from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from decouple import config
import random
from .models import Clothings, PhoneAndAccessories, HomeAndOffice, HealthAndBeauty, Gaming, Cart, AddProduct
from .forms import ClothingsForm, AddProductForm, PhoneAndAccessoriesForm, GamingForm, HomeAndOfficeForm, HealthAndBeautyForm, CartForm
from users.models import CustomUser
from .decorators import for_admins


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

@login_required(login_url='login')
def cart(request):
    search_input = request.GET.get('search_input')
    print('search......',search_input)
    if search_input == None:
        cart = Cart.objects.all()
    else:
        cart = Cart.objects.filter(title__contains=search_input)
    context = {'cart': cart}
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def phones_accessories(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    print('search......', cart_input, search_input, request.user.username)
    if cart_input != None:
        item = PhoneAndAccessories.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        Cart.objects.create(customer=user,name=item.name,price=item.price, in_stock=item.in_stock)
    if search_input == None:
        phones = PhoneAndAccessories.objects.all()
    else:
        phones = PhoneAndAccessories.objects.filter(name__icontains=search_input)
    context = {'phones': phones}
    return render(request, 'all_phones.html', context)


@login_required(login_url='login')
@for_admins
def edit_phones(request, id):
    phones = get_object_or_404(PhoneAndAccessories, id=id)
    form = PhoneAndAccessoriesForm(instance=phones)
    if request.method == 'POST':
        form = PhoneAndAccessoriesForm(request.POST, instance=phones)
        if form.is_valid():
            form.save()
            return redirect('phones_accessories')
    return render(request, 'edit_phones.html', {'form': form, 'id': id})


@login_required(login_url='login')
def all_clothings(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    print('search......',cart_input, search_input, request.user.username)
    if cart_input != None:
        item = Clothings.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        Cart.objects.create(customer=user, name=item.name, price=item.price, in_stock=item.in_stock,discounted_price=discounted_price)
    if search_input == None:
        clothings = Clothings.objects.all()
    else:
        clothings = Clothings.objects.filter(name__icontains=search_input)
    context = {'clothings': clothings}
    return render(request, 'all_clothings.html', context)


@login_required(login_url='login')
@for_admins
def edit_clothings(request, id):
    clothings = get_object_or_404(Clothings, id=id)
    form = Clothings(instance=clothings)
    if request.method == 'POST':
        form = Clothings(request.POST, instance=clothings)
        if form.is_valid():
            form.save()
            return redirect('edit_clothings')
    return render(request, 'edit_clothings.html', {'form': form, 'id': id})

@login_required(login_url='login')
def all_clothings(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    print('search......',cart_input, search_input, request.user.username)
    if cart_input != None:
        item = Clothings.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        Cart.objects.create(customer=user, name=item.name, price=item.price, in_stock=item.in_stock,discounted_price=discounted_price)
    if search_input == None:
        clothings = Clothings.objects.all()
    else:
        clothings = Clothings.objects.filter(name__icontains=search_input)
    context = {'clothings': clothings}
    return render(request, 'all_clothings.html', context)


@login_required(login_url='login')
@for_admins
def edit_clothings(request, id):
    _ = get_object_or_404(Clothings, id=id)
    form = ClothingsForm(instance=_)
    if request.method == 'POST':
        form = ClothingsForm(request.POST, instance=_)
        if form.is_valid():
            form.save()
            return redirect('clothings')
    return render(request, 'edit_clothings.html', {'form': form, 'id': id})

@login_required(login_url='login')
def gaming(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    print('search......', cart_input, search_input, request.user.username)
    if cart_input != None:
        item = Gaming.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        Cart.objects.create(customer=user, name=item.name, price=item.price, in_stock=item.in_stock,discounted_price=discounted_price)
    if search_input == None:
        gamings = Gaming.objects.all()
    else:
        gamings = Gaming.objects.filter(name__icontains=search_input)
    context = {'gamings': gamings}
    return render(request, 'gaming.html', context)


@login_required(login_url='login')
@for_admins
def edit_game_products(request, id):
    _ = get_object_or_404(Gaming, id=id)
    form = GamingForm(instance=_)
    if request.method == 'POST':
        form = GamingForm(request.POST, instance=_)
        if form.is_valid():
            form.save()
            return redirect('gaming')
    return render(request, 'edit_gamings.html', {'form': form, 'id': id})

@login_required(login_url='login')
def health_beauty(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    print('search......', cart_input, search_input, request.user.username)
    if cart_input != None:
        item = HealthAndBeauty.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        Cart.objects.create(customer=user, name=item.name, price=item.price, in_stock=item.in_stock,discounted_price=discounted_price)
    if search_input == None:
        items = HealthAndBeauty.objects.all()
    else:
        items = HealthAndBeauty.objects.filter(name__icontains=search_input)
    context = {'items': items}
    return render(request, 'health_beauty.html', context)


@login_required(login_url='login')
@for_admins
def edit_health_beauty(request, id):
    _ = get_object_or_404(HealthAndBeauty, id=id)
    form = HealthAndBeautyForm(instance=_)
    if request.method == 'POST':
        form = HealthAndBeautyForm(request.POST, instance=_)
        if form.is_valid():
            form.save()
            return redirect('health_beauty')
    return render(request, 'edit_health_beauty.html', {'form': form, 'id': id})


@login_required(login_url='login')
@for_admins
def add_products(request):
    if request.method == 'GET':
        form = AddProductForm()
        return render(request, 'add_products.html', context={'form': form})
    elif request.method == 'POST':
        form = AddProductForm(request.POST)
        category, name, price = request.POST.get('category'), request.POST.get('name'), request.POST.get('price')
        in_stock, image_name, discounted_price = request.POST.get('in_stock'), request.POST.get('image_name'), request.POST.get('discounted_price')
        # add inserted product to its respective category table
        if category == 'Clothings': 
            Clothings.objects.create(name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'PhoneAndAccessories': 
            PhoneAndAccessories.objects.create(name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'HomeAndOffice':
            HomeAndOffice.objects.create(name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'HealthAndBeauty':
            HealthAndBeauty.objects.create(name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'Gaming':
            Gaming.objects.create(name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        if form.is_valid():
            form.save()
            return redirect('add_products')
        else: return render(request, 'add_products.html', {'form': form})



# @login_required(login_url='login')
# def clothings_detail(request, id):
#     clothings = get_object_or_404(clothings, id=id)
#     form = ClothingsForm(instance=clothings)
#     context = {'form':form, 'id': id}
#     return render(request, 'clothings_detail.html', context)

# @login_required(login_url='login')
# def delete_clothings(request, id):
#     clothings = Clothings.objects.get(id=id)
#     clothings.delete()
#     return redirect('clothings')



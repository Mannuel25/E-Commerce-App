from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
import random, time
from .models import Clothings, PhoneAndAccessories, HomeAndOffice, HealthAndBeauty, Gaming, Cart, AllProducts
from .forms import ClothingsForm, AllProductsForm, PhoneAndAccessoriesForm, GamingForm, HomeAndOfficeForm, HealthAndBeautyForm, CartForm
from users.models import CustomUser
from .decorators import for_admins


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

def purchase_item(request, id):
    _ = Cart.objects.get(id=id)
    if _.category == 'Clothings':
        _a = Clothings.objects.get(name=_.name)
        print(_a.in_stock)
    elif _.category == 'PhoneAndAccessories':
        _a = PhoneAndAccessories.objects.get(name=_.name)
        print(_a.in_stock)
    elif _.category == 'HomeAndOffice':
        _a = HomeAndOffice.objects.get(name=_.name)
        print(_a.in_stock)
    elif _.category == 'HealthAndBeauty':
        _a = HealthAndBeauty.objects.get(name=_.name)
        print(_a.in_stock)
    elif _.category == 'Gaming':
        _a = Gaming.objects.get(name=_.name)
        print(_a.in_stock)
    _a.in_stock -= _.no_of_orders
    _a.save()
    time.sleep(1.5)
    _.delete()
    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    get_red_quan, get_inc_quan = request.GET.get('reduce_quantity'), request.GET.get('increase_quantity')
    purchase_ = request.GET.get('purchase')
    search_input = request.GET.get('search_input')
    if get_red_quan:
        user = CustomUser.objects.get(username=request.user.username)
        _ = Cart.objects.get(customer=user, name=get_red_quan)
        _.no_of_orders -= 1
        if _.discounted_price:
            total = _.no_of_orders * int(''.join(i for i in _.discounted_price.split(',')).strip())
            _.total_amount = f"{total:,d}"
        else:
            total = _.no_of_orders * int(''.join(i for i in _.price.split(',')).strip())
            _.total_amount = f"{total:,d}"
        _.delete() if _.no_of_orders == 0 else _.save()
    if get_inc_quan:
        user = CustomUser.objects.get(username=request.user.username)
        _ = Cart.objects.get(customer=user, name=get_inc_quan)
        _.no_of_orders += 1
        if _.discounted_price:
            total = _.no_of_orders * int(''.join(i for i in _.discounted_price.split(',')).strip())
            _.total_amount = f"{total:,d}"
        else:
            total = _.no_of_orders * int(''.join(i for i in _.price.split(',')).strip())
            _.total_amount = f"{total:,d}"
        _.save()
    if search_input:
        cart = Cart.objects.filter(name__icontains=search_input)
    else:
        cart = Cart.objects.all()
    context = {'cart': cart}
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def delete_cart_items(request, id):
    _ = Cart.objects.get(id=id)
    _.delete()
    return redirect('cart')


def phones_accessories(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = AllProducts.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            _ = Cart.objects.get(name=item.name)
            _.no_of_orders += 1
            _.save()
        else:
            Cart.objects.create(customer=user, name=item.name, price=item.price, discounted_price=item.discounted_price, image_name=item.image_name, category=item.category)
    if search_input:
        phones = PhoneAndAccessories.objects.filter(name__icontains=search_input)
    else:
        phones = PhoneAndAccessories.objects.all()
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


def all_clothings(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = AllProducts.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            _ = Cart.objects.get(name=item.name)
            _.no_of_orders += 1
            _.save()
        else:
            Cart.objects.create(customer=user, name=item.name, price=item.price, discounted_price=item.discounted_price, image_name=item.image_name, category=item.category)
    else:
        items = Clothings.objects.all()
    if search_input:
        items = Clothings.objects.filter(name__icontains=search_input)
    else:
        items = Clothings.objects.all()
    context = {'items': items}
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


def gaming(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = AllProducts.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            _ = Cart.objects.get(name=item.name)
            _.no_of_orders += 1
            _.save()
        else:
            Cart.objects.create(customer=user, name=item.name, price=item.price, discounted_price=item.discounted_price, image_name=item.image_name, category=item.category)
    if search_input:
        gamings = Gaming.objects.filter(name__icontains=search_input)
    else:
        gamings = Gaming.objects.all()
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


def health_beauty(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = AllProducts.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            _ = Cart.objects.get(name=item.name)
            _.no_of_orders += 1
            _.save()
        else:
            Cart.objects.create(customer=user, name=item.name, price=item.price, discounted_price=item.discounted_price, image_name=item.image_name, category=item.category)
    if search_input:
        items = HealthAndBeauty.objects.filter(name__icontains=search_input)
    else:
        items = HealthAndBeauty.objects.all()
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


def home_office(request):
    cart_input = request.GET.get('cart_input')
    search_input = request.GET.get('search_input')
    if cart_input:
        item = AllProducts.objects.get(name=cart_input)
        user = CustomUser.objects.get(username=request.user.username)
        check_item = Cart.objects.filter(name=item.name)
        if check_item.exists():
            _ = Cart.objects.get(name=item.name)
            _.no_of_orders += 1
            _.save()
        else:
            Cart.objects.create(customer=user, name=item.name, price=item.price, discounted_price=item.discounted_price, image_name=item.image_name, category=item.category)
    if search_input:
        items = HomeAndOffice.objects.filter(name__icontains=search_input)
    else:
        items = HomeAndOffice.objects.all()
    context = {'items': items}
    return render(request, 'home_office.html', context)


@login_required(login_url='login')
@for_admins
def edit_home_office(request, id):
    _ = get_object_or_404(HomeAndOffice, id=id)
    form = HomeAndOfficeForm(instance=_)
    if request.method == 'POST':
        form = HomeAndOfficeForm(request.POST, instance=_)
        if form.is_valid():
            form.save()
            return redirect('home_office')
    return render(request, 'edit_home_office.html', {'form': form, 'id': id})


@login_required(login_url='login')
@for_admins
def add_products(request):
    if request.method == 'GET':
        form = AllProductsForm()
        return render(request, 'add_products.html', context={'form': form})
    elif request.method == 'POST':
        form = AllProductsForm(request.POST)
        category, name, price = request.POST.get(
            'category'), request.POST.get('name'), request.POST.get('price')
        in_stock, image_name, discounted_price = request.POST.get(
            'in_stock'), request.POST.get('image_name'), request.POST.get('discounted_price')
        # add inserted product to its respective category table
        if category == 'Clothings':
            Clothings.objects.create(name=name, price=price, in_stock=in_stock,image_name=image_name, discounted_price=discounted_price)
        elif category == 'PhoneAndAccessories':
            PhoneAndAccessories.objects.create(
                name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'HomeAndOffice':
            HomeAndOffice.objects.create(
                name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'HealthAndBeauty':
            HealthAndBeauty.objects.create(
                name=name, price=price, in_stock=in_stock, image_name=image_name, discounted_price=discounted_price)
        elif category == 'Gaming':
            Gaming.objects.create(name=name, price=price, in_stock=in_stock,image_name=image_name, discounted_price=discounted_price)
        if form.is_valid():
            form.save()
            return redirect('add_products')
        else:
            return render(request, 'add_products.html', {'form': form})


@login_required(login_url='login')
@for_admins
def delete_phone_accessories(request, id):
    _ = PhoneAndAccessories.objects.get(id=id)
    _.delete()
    return redirect('phones_accessories')


@login_required(login_url='login')
@for_admins
def delete_clothings(request, id):
    _ = Clothings.objects.get(id=id)
    _.delete()
    return redirect('clothings')


@login_required(login_url='login')
@for_admins
def delete_gaming(request, id):
    _ = Gaming.objects.get(id=id)
    _.delete()
    return redirect('gaming')


@login_required(login_url='login')
@for_admins
def delete_health_beauty(request, id):
    _ = HealthAndBeauty.objects.get(id=id)
    _.delete()
    return redirect('health_beauty')


@login_required(login_url='login')
@for_admins
def delete_home_office(request, id):
    _ = HomeAndOffice.objects.get(id=id)
    _.delete()
    return redirect('home_office')

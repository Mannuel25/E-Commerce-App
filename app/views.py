from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from decouple import config
import random
from .models import Clothings, PhoneAndAccessories, HomeAndOffice, HealthAndBeauty, Gaming
from .forms import ClothingsForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

@login_required(login_url='login')
def all_clothings(request):
    search_input = request.GET.get('search-area')
    print('search......',search_input)
    if search_input == None:
        clothings = Clothings.objects.all()
    else:
        clothings = Clothings.objects.filter(title__contains=search_input)
    context = {'clothings': clothings}
    return render(request, 'all_clothings.html', context)

login_required(login_url='login')
def add_clothings(request):
    if request.method == 'GET':
        form = ClothingsForm()
        return render(request, 'add_clothings.html', context={'form': form})
    elif request.method == 'POST':
        form = ClothingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clothings')
        else: return render(request, 'add_clothings.html', {'form': form})


# @login_required(login_url='login')
# def edit_clothings(request, id):
#     clothings = get_object_or_404(Clothings, id=id)
#     form = ClothingsForm(instance=clothings)
#     if request.method == 'POST':
#         form = ClothingsForm(request.POST, instance=clothings)
#         if form.is_valid():
#             form.save()
#             return redirect('clothings')
#     return render(request, 'edit_clothings.html', {'form': form, 'id': id})

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



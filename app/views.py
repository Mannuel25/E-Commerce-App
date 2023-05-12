from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from googleapiclient.discovery import build
from decouple import config
import random


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

from django.shortcuts import render
from django.views.generic import ListView
from .models import Problem


class HomePageView(ListView):
    template_name = 'home.html'
    model = Problem
    context_object_name = 'problems'

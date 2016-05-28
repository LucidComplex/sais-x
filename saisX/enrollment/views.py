from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Student

class HomeView (TemplateView):
    model = Student
    template_name = 'enrollment/home.html'

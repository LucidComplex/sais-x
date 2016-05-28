from django.shortcuts import render
from django.view.generic import TemplateView, ListVew
from enrollment.views import Student

class HomeView (TemplateView)
    model = Student
    template = 'enrollment/home.html'

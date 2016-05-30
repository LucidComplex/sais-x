from django.shortcuts import render
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView, ListView
from .models import Student
from .forms import UserLoginForm, StudentForm

class HomeView(TemplateView):
    model = Student
    template_name = 'enrollment/home.html'


class LoginView(FormView):
    template_name = "enrollment/login.html"
    form_class = UserLoginForm
    success_view_name = 'enrollment:home'

    def get(self, request, *args, **kwargs):
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.cleaned_data['user']
        login(self.request, user)

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return next

        else:
            return reverse(self.success_view_name)


class ScheduleView(TemplateView):
    model = Student
    template_name = 'enrollment/schedule.html'


class GradesView(ListView):
    model = Student
    template_name = 'enrollment/viewgrades.html'


class EditView(TemplateView):
    model = Student
    template_name = 'enrollment/edit_info.html'


class ProfileView(TemplateView):
    model = Student
    template_name = 'enrollment/profile.html'

class CoursesView(TemplateView):
    template_name = 'enrollment/courses.html'

class SyllabusView(TemplateView):
    template_name = 'enrollment/syllabus.html'

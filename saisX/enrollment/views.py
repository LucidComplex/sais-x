from django.shortcuts import render
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView, ListView
from enrollment.models import Course, Student
from enrollment.forms import UserLoginForm, StudentForm

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
    template_name = 'enrollement/schedule.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context['schedule'] = None
        return context


class GradesView(ListView):
    model = Student
    template_name = 'enrollment/viewgrades.html'


class EditView(TemplateView):
    model = Student
    template_name = 'enrollment/edit_info.html'

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['studentform'] = StudentForm(isinstance = self.request.student, data=self.request.POST)

        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        studentform = context['studentform']

        if studentform.is_valid():
            studentform.save()
        else:
            print studentform.errors

        return self.render_to_response(context)


class ProfileView(TemplateView):
    model = Student
    template_name = 'enrollment/profile.html'


class CourseListView(ListView):
    model = Course
    paginate_by = 6
    template_name = 'enrollment/course_list.html'

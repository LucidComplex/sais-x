from . import views
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'home$', views.HomeView.as_view(), name='home'),
    url(r'login$', views.LoginView.as_view(), name="login"),
    url(r'profile$', views.ProfileView.as_view(), name='profile'),
    url(r'grades$', views.GradesView.as_view(), name='grades'),
    url(r'schedule$', views.ScheduleView.as_view(), name='schedule'),
    url(r'manage', views.ManageView.as_view(), name='manage'),
    url(r'edit$', views.EditView.as_view(), name='edit'),
    url(r'enroll$', views.EnrollView.as_view(), name='enroll'),
    url(r'enlist$', views.EnlistView.as_view(), name='enlist'),
    url(r'courses$', views.CoursesView.as_view(), name='courses'),
]


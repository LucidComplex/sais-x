from . import views
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'home$', views.HomeView.as_view(), name='home'),
    url(r'login$', views.LoginView.as_view(), name='login'),
    url(r'course/list$', views.CourseListView.as_view(), name='course_list')
]

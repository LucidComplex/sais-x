from . import views
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'home$', views.HomeView.as_view(), name='home'),
]

from django.urls import path
from django.urls import include, re_path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from requests import request
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('login', views.login_page, name='login'),
    path("", views.home__x, name="home"),
    path("upload", views.home_view, name="upload"),
    path("myprofile/", views.myprofile, name="myprofile"),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('read_now', views.read_now, name='read_now'),
    re_path(
        'password',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    re_path(r'^logout/$', views.custom_logout, name='logout')
]
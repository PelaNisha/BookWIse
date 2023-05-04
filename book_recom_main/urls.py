from django.urls import path
from book_recom_main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload", views.home_view, name="upload"),
    path("myprofile", views.myprofile, name="myprofile"),
    path('add_to_cart', views.add_to_cart, name='add_to_cart')   




]
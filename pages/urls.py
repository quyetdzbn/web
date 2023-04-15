from django.urls import path
from . import views
# from .views import SignUpView
# from . django.contrib import admin

urlpatterns = [
    path("", views.home,name="home"),
    path("register/", views.register,name="register"),
    path("introduce/", views.introduce,name="introduce"),
    path("login/", views.loginPage,name="login"),
    path("search/", views.search,name="search"),
    path("logout/", views.logoutPage,name="logout"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("cart/update_item/", views.updateItem, name="update_item"),
    path("search/update_item/", views.updateItem, name="update_item"),
    # path("signup/", SignUpView.as_view(), name="signup"),
]   
# TimeoutError
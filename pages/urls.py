from django.urls import path
from . import views
# from .views import SignUpView
# from . django.contrib import admin

urlpatterns = [
    path("", views.home,name="home"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    # path("signup/", SignUpView.as_view(), name="signup"),
]   
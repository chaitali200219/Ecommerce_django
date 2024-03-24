

from django.urls import path
from accounts.views import login_page
from accounts.views import register_page,activate_email,add_to_cart,cart,remove_cart

urlpatterns = [
    path('login/' ,login_page,name="login"),
    path('register/' ,register_page,name="register"),
    path('activate/<email_token>/',activate_email,name='activate_email'),
    path('cart/',cart,name="cart"),
    path('add_to_cart/<uid>/',add_to_cart,name="add_to_cart"),
    path('remove-cart/<cart_item_uid>/',remove_cart,name="remove_Cart"),
    # path('remove-coupon/cart_id/',remove_coupon ,name="remove_coupon")
    
]
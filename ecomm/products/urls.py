# from django.urls import path
# from products.views import get_products


# urlpatterns = [
#     path('<slug>/',get_products,name="get_product"),
# ]

from django.urls import path
from products.views import get_products

urlpatterns = [
    path('', get_products, name="get_products"),  # URL pattern for /products
    path('<slug>/', get_products, name="get_product"),  # URL pattern for product details
]

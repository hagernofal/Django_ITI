

from django.urls import path 
from . import views

# create routes for product
"""
    get /products/ --> all products
    post /products/ --> create new product
    get /products/id --> get product
    put /products/id --> update product
    delete /products/id --> delete product

"""


urlpatterns = [
    path('', views.product_list_create),
    path('<int:id>/', views.product_detail),
]
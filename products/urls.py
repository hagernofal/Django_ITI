
from django.urls import path
from products.views import  (index,product_profile,create,delete,edit)

urlpatterns = [
    path('', index, name='products'),
    path('<int:id>/', product_profile, name='product.profile'),
    path('create/', create, name='product.create'),
    path('delete/<int:id>', delete, name='products.delete'),
    path('edit/<int:id>', edit, name='products.edit')
]
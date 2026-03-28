from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list_create),
    path('<int:id>/', views.category_detail),
]
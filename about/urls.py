
from django.urls import path
from about.views import  (index)

urlpatterns = [
    path('', index, name='about')
]

from django.urls import path
from category.views import index, category_profile

urlpatterns = [
    path('', index, name='categories'),
    path('<int:id>/', category_profile, name='category.profile'),
]

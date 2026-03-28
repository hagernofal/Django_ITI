from django.db import models
from django.shortcuts import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True , null = True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to="products/images" ,null =True , blank=True)
    category=  models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,
                                related_name="products")
    def __str__(self):
        return f'{self.name}'
    
    @property
    def image__url(self):
        return f'/media/{self.image}'
    
    @property
    def show__url(self):
        return reverse("product.profile", args=[self.id])
    
    @property
    def delete_url(self):
        return reverse("products.delete", args=[self.id])
    
    @property
    def edit_url(self):
        return reverse("products.edit", args=[self.id])
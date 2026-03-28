from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    logo = models.ImageField(upload_to="categories/logos" ,null =True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null = True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def logo_url(self):
        return f'/media/{self.logo}'
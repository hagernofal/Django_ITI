from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404,redirect
from category.models import Category
from products.models import Product



def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html",
            context={"products": products})

def product_profile(request, id):
    product = get_object_or_404(Product, pk=id)  
    return render(request, "products/product_profile.html", context={"product": product})


def create(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        stock = request.POST.get("stock")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category = request.POST.get("category")
        category = Category.objects.filter(pk=category).first()
        product = Product(
                name=name,
                stock=stock,
                price=price,
                description=description,
                image = image,
                category = category or None

        )
        product.save()
        return redirect(product.show__url)  

    return render(request, "products/create.html",
                context={"categories":categories})

def delete(request, id):
    product= get_object_or_404(Product, pk=id)
    product.delete() 
    return redirect("products")

def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    categories = Category.objects.all()

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.stock = request.POST.get("stock")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        
        if request.FILES.get("image"):
            product.image = request.FILES.get("image")

        category_id = request.POST.get("category")
        product.category = Category.objects.filter(pk=category_id).first()

        product.save()
        return redirect(product.show__url)

    return render(request, "products/edit.html", {
        "product": product,
        "categories": categories
    })




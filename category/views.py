from django.shortcuts import render , get_object_or_404
from category.models import Category
# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, "categories/index.html",
            context={"categories": categories})

def category_profile(request, id):
    category = get_object_or_404(Category, pk=id)
    return render(request, "categories/category_profile.html", context={"category": category})


# def create(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         stock = request.POST.get("stock")
#         price = request.POST.get("price")
#         description = request.POST.get("description")
#         image = request.FILES.get("image")
#         product = Product(
#                 name=name,
#                 stock=stock,
#                 price=price,
#                 description=description,
#                 image = image
#         )
#         product.save()
#         return redirect(product.show__url)  

#     return render(request, "products/create.html")
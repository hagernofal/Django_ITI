from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from .serializers import ProductModelSerializer


@api_view(['GET', 'POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == 'GET':
        return Response(ProductModelSerializer(product).data)

    elif request.method == 'PATCH':
        serializer = ProductModelSerializer(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return Response({"message": "Deleted"}, status=204)
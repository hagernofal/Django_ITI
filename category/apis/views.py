from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from category.models import Category
from .serializers import CategoryModelSerializer


@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def category_detail(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == 'GET':
        return Response(CategoryModelSerializer(category).data)

    elif request.method == 'PATCH':
        serializer = CategoryModelSerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return Response({"message": "Deleted"}, status=204)
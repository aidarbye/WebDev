from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .serializers import CategorySerializer, ProductSerializer
from .models import Product, Category
from django.http import HttpResponse, Http404, JsonResponse

# Create your views here.
@require_http_methods(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_one_product(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found')
    serializer = ProductSerializer(product, many = False)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def get_one_category(request,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse('Category not found')
    serializer = CategorySerializer(category, many=False)
    return JsonResponse(serializer.data, safe = False)

@require_http_methods(["GET"])
def list_of_products_by_category(request,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse('Category not found')
    products = category.products.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)
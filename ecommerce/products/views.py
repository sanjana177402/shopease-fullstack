from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductListCreate(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()

        search = request.GET.get('search')
        if search:
            products = products.filter(name__icontains=search)

        category = request.GET.get('category')
        if category:
            products = products.filter(category__name=category)

        sort = request.GET.get('sort')
        if sort == 'low':
            products = products.order_by('price')
        elif sort == 'high':
            products = products.order_by('-price')

        page = int(request.GET.get('page', 1))
        limit = 5
        start = (page - 1) * limit
        end = start + limit
        products = products[start:end]

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductDetail(APIView):

    permission_classes = [AllowAny]

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None

    def get(self, request, id):
        product = self.get_object(id)
        if not product:
            return Response({"error": "Not found"}, status=404)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = self.get_object(id)
        if not product:
            return Response({"error": "Not found"}, status=404)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        product = self.get_object(id)
        if not product:
            return Response({"error": "Not found"}, status=404)
        product.delete()
        return Response({"message": "Deleted successfully"})


class AllProducts(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WishlistItem
from users.models import User
from products.models import Product

class WishlistView(APIView):

    def get(self, request):
        user_id = request.query_params.get("userId")
        if not user_id:
            return Response({"error": "userId required"}, status=400)
        items = WishlistItem.objects.filter(user_id=user_id)
        data = [{
            "productId": item.product.id,
            "name": item.product.name,
            "price": item.product.price,
            "image": item.product.image
        } for item in items]
        return Response(data)

    def post(self, request):
        user_id = request.data.get("userId")
        product_id = request.data.get("productId")
        if not user_id or not product_id:
            return Response({"error": "userId and productId required"}, status=400)
        try:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
        except:
            return Response({"error": "User or product not found"}, status=404)
        item, created = WishlistItem.objects.get_or_create(user=user, product=product)
        if created:
            return Response({"message": "Added to wishlist"})
        return Response({"message": "Already in wishlist"})

    def delete(self, request, productId):
        user_id = request.query_params.get("userId")
        if not user_id:
            return Response({"error": "userId required"}, status=400)
        try:
            item = WishlistItem.objects.get(user_id=user_id, product_id=productId)
            item.delete()
            return Response({"message": "Removed from wishlist"})
        except WishlistItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
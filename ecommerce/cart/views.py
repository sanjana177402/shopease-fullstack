from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CartItem
from users.models import User


class AddToCart(APIView):

    def post(self, request):
        user_id = request.data.get("userId")
        product_id = request.data.get("productId")
        quantity = request.data.get("quantity")

        if not user_id or not product_id or not quantity:
            return Response({"error": "userId, productId and quantity required"}, status=400)

        try:
            quantity = int(quantity)
        except:
            return Response({"error": "Quantity must be number"}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        item, created = CartItem.objects.get_or_create(
            user=user,
            product_id=product_id,
            defaults={"quantity": quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

        return Response({"message": "Added to cart"})


class CartView(APIView):

    def get(self, request):
        user_id = request.query_params.get("userId")

        if not user_id:
            return Response({"error": "userId required"}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        items = CartItem.objects.filter(user=user)

        data = []
        total_price = 0

        for item in items:
            item_total = item.product.price * item.quantity
            total_price += item_total
            data.append({
                "productId": item.product.id,
                "name": item.product.name,
                "quantity": item.quantity,
                "price": item.product.price,
                "total": item_total,
                "image": item.product.image
            })

        return Response({
            "items": data,
            "totalPrice": total_price
        })


class UpdateCart(APIView):

    def put(self, request):
        user_id = request.data.get("userId")
        product_id = request.data.get("productId")
        quantity = request.data.get("quantity")

        if not user_id or not product_id or not quantity:
            return Response({"error": "userId, productId and quantity required"}, status=400)

        try:
            quantity = int(quantity)
        except:
            return Response({"error": "Quantity must be number"}, status=400)

        try:
            item = CartItem.objects.get(user_id=user_id, product_id=product_id)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)

        item.quantity = quantity
        item.save()

        return Response({"message": "Cart updated"})


class RemoveFromCart(APIView):

    def delete(self, request, productId):
        user_id = request.query_params.get("userId")

        if not user_id:
            return Response({"error": "userId required"}, status=400)

        try:
            item = CartItem.objects.get(user_id=user_id, product_id=productId)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)

        item.delete()
        return Response({"message": "Item removed"})
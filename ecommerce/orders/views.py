from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OrderSerializer   
from .models import Order, OrderItem
from cart.models import CartItem
from users.models import User


class OrderListCreate(APIView):

    def post(self, request):
        user_id = request.data.get("userId")

        user = User.objects.get(id=user_id)
        cart_items = CartItem.objects.filter(user=user)

       
        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        total = 0

        order = Order.objects.create(user=user, totalAmount=0)

        for item in cart_items:
            item_total = item.product.price * item.quantity
            total += item_total

            OrderItem.objects.create(
                order=order,
                product=item.product,
                qty=item.quantity
            )

       
        order.totalAmount = total
        order.save()

        
        cart_items.delete()

        return Response({
            "message": "Order placed",
            "total": total
        })

       

    def get(self, request):
        user_id = request.query_params.get("userId")

        orders = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)


class OrderDetail(APIView):

    def get(self, request, id):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)

        return Response(serializer.data)


class AdminOrderList(APIView):

    def get(self, request):
        orders = Order.objects.all().order_by('-createdAt')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class UpdateOrderStatus(APIView):

    def put(self, request, id):
        status_value = request.data.get("status")

        VALID_STATUS = ["placed", "shipped", "delivered", "cancelled"]

        if status_value not in VALID_STATUS:
            return Response({"error": "Invalid status"}, status=400)

        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        order.status = status_value
        order.save()

        return Response({
            "message": "Status updated",
            "orderId": order.id,
            "newStatus": order.status
        })
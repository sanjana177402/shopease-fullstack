from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    productId = serializers.IntegerField(source='product.id')

    class Meta:
        model = OrderItem
        fields = ['productId', 'qty']


class OrderSerializer(serializers.ModelSerializer):

    userId = serializers.IntegerField(source='user.id')

    items = OrderItemSerializer(many=True)

    total_price = serializers.IntegerField(source='totalAmount')

    
    image = serializers.SerializerMethodField()

    class Meta:
        model = Order

        fields = [
            'id',
            'userId',
            'items',
            'total_price',
            'status',
            'createdAt',
            'image'
        ]

    
    def get_image(self, obj):

        first_item = obj.items.first()

        if first_item:
            return first_item.product.image

        return ""
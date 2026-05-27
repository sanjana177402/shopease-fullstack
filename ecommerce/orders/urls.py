from django.urls import path
from .views import (
    OrderListCreate, OrderDetail,
    AdminOrderList, UpdateOrderStatus
)

urlpatterns = [
    path('', OrderListCreate.as_view()),                
    path('<int:id>/', OrderDetail.as_view()),           

    
    path('admin/orders/', AdminOrderList.as_view()),     
    path('admin/orders/<int:id>/status/', UpdateOrderStatus.as_view()),
]
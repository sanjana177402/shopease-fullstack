from django.urls import include, path
from .views import CartView, AddToCart, UpdateCart, RemoveFromCart

urlpatterns = [
    path('', CartView.as_view()),                 
    path('add/', AddToCart.as_view()),           
    path('update/', UpdateCart.as_view()),       
    path('remove/<int:productId>/', RemoveFromCart.as_view()), 
    
]

from django.urls import path
from .views import CartView, AddToCart, UpdateCart, RemoveFromCart

urlpatterns = [
    path('', CartView.as_view()),                 # GET /cart
    path('add/', AddToCart.as_view()),           # POST /cart/add
    path('update/', UpdateCart.as_view()),       # PUT /cart/update
    path('remove/<int:productId>/', RemoveFromCart.as_view()),  # DELETE
]
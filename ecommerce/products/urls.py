from django.urls import path
from .views import ProductListCreate, ProductDetail , AllProducts 

urlpatterns = [
    path('', ProductListCreate.as_view()),
    path('<int:id>/', ProductDetail.as_view()),
    path('all-products/',AllProducts.as_view()),
]
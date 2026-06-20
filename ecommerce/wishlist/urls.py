from django.urls import path
from .views import WishlistView

urlpatterns = [
    path('', WishlistView.as_view()),
    path('<int:productId>/', WishlistView.as_view()),
]
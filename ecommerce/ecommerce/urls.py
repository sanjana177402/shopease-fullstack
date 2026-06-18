from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('products/', include ('products.urls')),
    path('cart/', include('cart.urls')),
    path('categories/', include('categories.urls')),
    path('orders/', include('orders.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='register.html')),
    path('login/', TemplateView.as_view(template_name='login.html')),
    path('cart/', TemplateView.as_view(template_name='cart.html')),
    path('orders/', TemplateView.as_view(template_name='orders.html')),
    path('payment/', TemplateView.as_view(template_name='payment.html')),
    path('wishlist/', TemplateView.as_view(template_name='wishlist.html')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import CategoryListCreate

urlpatterns = [
    path('', CategoryListCreate.as_view()),
]
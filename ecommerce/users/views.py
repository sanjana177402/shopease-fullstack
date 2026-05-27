from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken  
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=400)

        if not check_password(password, user.password):
            return Response({"error": "Invalid credentials"}, status=400)

    
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Login successful",
            "userId": user.id,
            "access": str(refresh.access_token),   
            "refresh": str(refresh)                 
        })

from rest_framework.permissions import IsAuthenticated

class MeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # ← gets user directly from the JWT token
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        })

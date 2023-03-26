from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Ingredients, Post
from .serializers import PostSerializer, IngredientSerializer, UserSerializer, MyTokenObtainPairSerializer

# Create your views here.

class CreateUser(generics.CreateAPIView):
    model = get_user_model
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class IngredientList(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredients.objects.all()
    permissions_classes = [permissions.AllowAny]


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = IngredientSerializer
   queryset = Ingredients.objects.all()
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permissions_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
      print(request, request.user)
      request.data['user'] = request.user.username
      return self.create(request, *args, **kwargs)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permissions_classes = [permissions.AllowAny]

    def put(self, request, *args, **kwargs):
      print(request)
      return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)




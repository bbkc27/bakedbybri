from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Ingredients, Post

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  def create(self, validated_data):

    user = UserModel.objects.create(
      username=validated_data['username'],
      password=validated_data['password']
    )

    return user


  class Meta:
    model = UserModel
    fields = ('id', 'username', "password")

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
    
class PostSerializer(serializers.ModelSerializer):
   
   ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredients.objects.all())
   author = UserSerializer(many = False, read_only=True)

   class Meta:
      model = Post
      fields = ('id','author', 'uuid', 'title', 'ingredients','duration','category','recipe')

class IngredientSerializer(serializers.ModelSerializer):
   
   post_list = PostSerializer(many=True, read_only=True)

   class Meta:
      model = Ingredients
      fields = ('id','name', 'post_list')
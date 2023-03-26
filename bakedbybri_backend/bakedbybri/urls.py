from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.CreateUser.as_view()),

    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
    path('ingredients/', views.IngredientList.as_view()),
    path('ingredients/<int:pk>', views.IngredientDetail.as_view(), name='ingredient_detail')

]
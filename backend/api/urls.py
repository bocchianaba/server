from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.registration import UserRegistrationView, UserLoginView, UserDetailView
from .views.product import (
    ProductDetailView, 
    ProductPostLikePushView, 
    ProductPostLikePopView, 
    ProductPostDisLikePushView,
    ProductPostDislikePopView, 
    ProductPostLovePushView, 
    ProductPostLovePopView,
    MyProductDetailView
)



urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('me', UserDetailView.as_view(), name='user_detail'),
    path('products', ProductDetailView.as_view(), name='all_products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/like/push/<int:pk>', ProductPostLikePushView.as_view(), name='product_like_push'),
    path('product/like/pop/<int:pk>', ProductPostLikePopView.as_view(), name='product_like_pop'),
    path('product/dislike/push/<int:pk>', ProductPostDisLikePushView.as_view(), name='product_dislike_push'),
    path('product/dislike/pop/<int:pk>', ProductPostDislikePopView.as_view(), name='product_dislike_pop'),
    path('product/love/push/<int:pk>', ProductPostLovePushView.as_view(), name='product_love_push'),
    path('product/love/pop/<int:pk>', ProductPostLovePopView.as_view(), name='product_love_pop'),
    path('myproducts', MyProductDetailView.as_view(), name='my_products'),
    path('myproducts/<int:pk>', MyProductDetailView.as_view(), name='update_my_product'),
]
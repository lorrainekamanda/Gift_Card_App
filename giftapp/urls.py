from django.urls import path
from .views import RegisterView, LoginView,ProductsView,ProductView,ProductCategoryView,ProductsCategoryView,WishlistsView,PasswordChangeView

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign_up'),
    path('sign-in/', LoginView.as_view(), name='sign_in'),
    path('products-view/', ProductsView.as_view(), name='products_view'),
    path('product/<pk>/', ProductView.as_view(), name='product_detail'),
    path('category-view/', ProductsCategoryView.as_view(), name='category_view'),
    path('category/<pk>/', ProductCategoryView.as_view(), name='category_detail'),
    path('wishlists-view/', WishlistsView.as_view(), name='wishlists_view'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
]
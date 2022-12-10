from django.urls import path
from .views import RegisterView, LoginView,ProductsView,ProductView

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='sign_up'),
    path('sign-in/', LoginView.as_view(), name='sign_in'),
    path('products-view/', ProductsView.as_view(), name='products_view'),
    path('product/<pk>/', ProductView.as_view(), name='product_detail'),
]
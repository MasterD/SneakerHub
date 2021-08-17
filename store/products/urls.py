from django.urls import path
from . import views
from .views import CreateProduct, ProductDetail, ProductListView, UpdateProductView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='view_products'),
    path('product/new/', CreateProduct.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', UpdateProductView.as_view(), name='product-update'),
]
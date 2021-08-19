from django.urls import path
from . import views
from .views import CreateProduct, ProductDetail, ProductListView, UpdateProductView, DeleteProductView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='view_products'),
    path('product/new/', CreateProduct.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', UpdateProductView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='product-delete'),
    path('product/<int:pk>/add_to_cart/', ProductDetail.as_view(), name='add_to_cart'),
]
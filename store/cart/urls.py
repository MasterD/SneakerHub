from django.urls import path
from . import views
from .views import AddToCart

urlpatterns = [
    path('cart/<int:pk>/add_to_cart/', AddToCart.as_view(), name='add_to_cart'),
]
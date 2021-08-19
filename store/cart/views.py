from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AddToCart(LoginRequiredMixin, CreateView):
    model = Cart
    fields = []
    template_name = 'cart/add_to_cart.html'
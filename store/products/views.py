from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['brand', 'model', 'description', 'image', 'price', 'category']
    template_name = 'products/sell_product.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
        

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/view_products.html'
    context_object_name = 'products'
    ordering = ['-date_created']
    paginate_by = 4

class UpdateProductView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Product
    fields = ['brand', 'model', 'description', 'image', 'price', 'category']
    template_name = 'products/sell_product.html'

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):

        product = self.get_object()

        if self.request.user == product.user:
            return True
        else:
            return False

class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/product'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.user:
            return True
        else:
            return False
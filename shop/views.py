from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from cart.forms import CartAddProductForm

from shop.models import Category, Product


class CategoryListView(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 2

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        category = None
        if self.kwargs.get('category_slug'):
            category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
            context['object_list'] = Product.objects.filter(category=category, available=True)[:self.paginate_by]

        context['categories'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        context['category'] = category

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()

        return context

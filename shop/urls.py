from django.urls import path
from shop.views import ProductDetail, CategoryListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='product_list'),
    path('category/<slug:category_slug>/', CategoryListView.as_view(), name='product_by_category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),

]

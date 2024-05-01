from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]

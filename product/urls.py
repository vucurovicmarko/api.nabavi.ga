from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]

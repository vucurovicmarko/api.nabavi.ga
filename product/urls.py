from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('latest-products/', views.LatestProductList.as_view()),
]

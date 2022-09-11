
from django.urls import path,include

from shop.api import CategoryViewset,ProductViewset

from .views import ProductDetail, ProductList, category, index
   
from rest_framework import routers
   
   
router = routers.SimpleRouter()
router.register('category',CategoryViewset,basename='category')
router.register('product',ProductViewset,basename='product')

   
urlpatterns = [
    path("", index, name="home"),
    path("shop/", ProductList.as_view(), name="product-list"),
<<<<<<< HEAD
    path("shop/<slug:slug>/details/",ProductDetail.as_view(), name="product-details"),
    path("category/<slug:category>",ProductList.as_view(),name="category_pots_list")     
=======
    path("shop/<slug:slug>/details/",
         ProductDetail.as_view(), name="product-details"),
    path('category',category,name='category'),
    # Les API
    path('api/',include(router.urls))
>>>>>>> b0cd4792772dece74b8c6a311086951fefc6f97d
]
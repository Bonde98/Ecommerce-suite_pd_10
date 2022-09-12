
from django.urls import path

from .views import ProductDetail, ProductList,  index
   

   
urlpatterns = [
    path("", index, name="home"),
    path("shop/", ProductList.as_view(), name="product-list"),

    path("shop/<slug:slug>/details/",ProductDetail.as_view(), name="product-details"),
    path("category/<slug:category>",ProductList.as_view(),name="category_pots_list") ,    

    path("shop/<slug:slug>/details/",
         ProductDetail.as_view(), name="product-details"),
    
    

]
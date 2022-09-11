
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shop.models import Category, Product



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ProductListtSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class ProductdetailSerialiazer(ModelSerializer):
    
    
    class Meta:
        model = Product
        fields = ['id','name','slug','image','description','price','created','updated']
     
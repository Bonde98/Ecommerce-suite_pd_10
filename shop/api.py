from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.models import Category, Product
#from rest_framework.permissions import IsAuthenticated


from shop.serializers import CategorySerializer, ProductListtSerializer,ProductdetailSerialiazer


class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    
    
    def get_queryset(self):
        return  Category.objects.all()
 
 
class ProductViewset(ReadOnlyModelViewSet):
    
    serializer_class = ProductListtSerializer
    detail_serializer_class = ProductdetailSerialiazer
    
    queryset = Product.objects.all()
    

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from order.models import Order, OrderItem

from order.serializers import OrderItemSerialaizer, OrderSerializer



class OrderViewset(ModelViewSet):
    
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.all()
    

class OrderItemViewset(ReadOnlyModelViewSet):
    serializer_class = OrderItemSerialaizer
    
    queryset = OrderItem.objects.all()
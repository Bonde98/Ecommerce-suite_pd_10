from rest_framework.serializers import ModelSerializer

from order.models import Order, OrderItem



class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
        
        
class OrderItemSerialaizer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
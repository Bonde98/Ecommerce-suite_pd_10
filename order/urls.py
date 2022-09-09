
from django.urls import path,include

from order.views import order_create, order_created

from rest_framework import routers
from .api import OrderItemViewset, OrderViewset

router = routers.SimpleRouter()
router.register('order',OrderViewset,basename='order')
router.register('orderitem',OrderItemViewset,basename='orderitem')

urlpatterns = [
    path("checkout/", order_create, name="order_create"),
    path("thanks/", order_created, name="order_created"),
    # Les API
    path('api/',include(router.urls))
]
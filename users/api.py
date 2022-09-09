from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from users.permissions import IsAdminAuthenticated

from users.srializers import CustomuserSerializer


class CustomuserViewset(ModelViewSet):
    
    serializer_class = CustomuserSerializer
    
    def get_queryset(self):
        return CustomUser.objects.all()
    
    
class AdminCustomuserViewset(ModelViewSet):
    
    serializer_class = CustomuserSerializer
    
    permission_classes = [IsAdminAuthenticated]
    
    def get_queryset(self):
        return CustomUser.objects.all()

from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class CustomuserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username','email']
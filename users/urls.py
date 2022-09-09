
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from users.views import SignUpView,connexion

from rest_framework import routers

from users.api import  AdminCustomuserViewset, CustomuserViewset

router = routers.SimpleRouter()
router.register('users',CustomuserViewset , basename="users")
router.register('admin/users',AdminCustomuserViewset, basename="admin-users")


urlpatterns = [
    
    path("signup/" ,  SignUpView.as_view (), name = "signup" ),
    path("connexion/",connexion,name="connexion"),
    path("logout/",LogoutView.as_view(),name="logout"),
    # Les API
    path('api/',include(router.urls)),
]


from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import SignUpView,connexion, bonde

urlpatterns = [
    path("signup/" ,  SignUpView.as_view (), name = "signup" ),
    path("connexion/",connexion,name="connexion"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("essaye/",bonde, name="essaye"),
]


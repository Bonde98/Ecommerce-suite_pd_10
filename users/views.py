
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .form import CustomUserCreationForm,LoginForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("connexion")
    template_name = "users/register.html"



def bonde(request):
    
    return render(request,"users/essaye.html")



def connexion(request):
    connexion = LoginForm(request.POST or None )
    if connexion.is_valid():
        email = connexion.cleaned_data.get("email") 
        password = connexion.cleaned_data.get("password")
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("cart_detail")
    return render(request,"users/connexion.html",{"connexion":connexion})


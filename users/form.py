from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from .models import CustomUser


class LoginForm(forms.Form):
      email = forms.CharField(label="Email",
                            widget= forms.TextInput
                            (attrs={"class":"form-control","placeholder":"Adresse email"}))
      password = forms.CharField(label="Mot de Passe",
                            widget= forms.PasswordInput
                           (attrs={"class":"form-control","placeholder":"Mot de passee"}))


class CustomUserCreationForm(UserCreationForm):
      name = forms.CharField(label="Prénom Nom",
                            widget= forms.TextInput
                            (attrs={"class":"form-control","placeholder":"Nom Compet"}))
      email = forms.CharField(label="Adress Email",
                            widget= forms.EmailInput
                            (attrs={"class":"form-control","placeholder":"Adresse email"}))
      password1 = forms.CharField(label="Password",
                            widget= forms.PasswordInput
                           (attrs={"class":"form-control","placeholder":"Mot de passe"}))
      password2 = forms.CharField(label="Confirm Password",
                            widget= forms.PasswordInput
                           (attrs={"class":"form-control","placeholder":"Confirmez le mot de passe"}))
      

      class Meta:
        model = CustomUser
        fields = ('name','email','password1','password2',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
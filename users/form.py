from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from .models import CustomUser


class LoginForm(forms.Form):
      email = forms.CharField(label="Email",
                            widget= forms.TextInput
                            (attrs={"class":"form-control"}))
      password = forms.CharField(label="Mot de Passe",
                            widget= forms.PasswordInput
                           (attrs={"class":"form-control"}))


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
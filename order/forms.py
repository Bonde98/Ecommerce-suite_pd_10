from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Name", widget=forms.TextInput({"class": "form-control py-3", "placeholder": "Nom complet"}))

    address = forms.CharField(
        label="Adress", widget=forms.TextInput({"class": "form-control py-3", "placeholder": "Adresse de livraison"}))

   
    phone = forms.CharField(
        label="Phone", widget=forms.TextInput({"class": "form-control py-3", "placeholder": "Telephone"}))

    class Meta:
        model = Order
        fields = ("full_name",  "address", "phone",)
from .models import *
from django import forms
# class ProductForms(forms.ModelForm):
class ProductForms(forms.ModelForm):
    class Meta:
        model = Prod
        fields = ('prodName','price','quantity')

        widgets = {
            'prodName': forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'step': 1.0}),
            'quantity' : forms.NumberInput(attrs={'step': 1.0}),

        }




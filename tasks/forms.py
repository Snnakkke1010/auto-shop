from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cat', 'image', 'about', 'price', 'in_stock']


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Search')
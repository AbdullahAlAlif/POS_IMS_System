from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','description','price','quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Force HTML attributes for quantity
        self.fields['quantity'].widget.attrs.update({'min': 1, 'value': 1})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

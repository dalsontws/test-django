from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your Title"}))

    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Description",
                                                               "class": "new-class",
                                                               "rows": 20, "cols": 50}))

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "new-class",
                                                               "rows": 20, "cols": 10}))
    price = forms.DecimalField(initial=199.99)

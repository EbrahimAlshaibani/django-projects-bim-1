from django.forms import ModelForm
from django import forms
from store.models import *
from django.utils.translation import gettext_lazy as _

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "name": _("name")
        }
        help_texts = {
            "name": _("Some useful help text."),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }
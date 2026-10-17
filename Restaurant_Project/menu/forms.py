from django import forms
from django.core.exceptions import ValidationError
from .models import MenuItem, Chef


class MenuItemForm(forms.ModelForm):
    """Form for creating and editing menu items."""
    
    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'chef', 'price', 'description', 'is_available']
    
    def clean_price(self):
        """Validate that price is greater than zero."""
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('Price must be greater than zero.')
        return price


class ChefForm(forms.ModelForm):
    """Form for creating and editing chefs."""
    
    class Meta:
        model = Chef
        fields = ['name', 'specialization']

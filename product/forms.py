from django import forms
from .models import InventoryItem


class DiscountForm(forms.Form):
    code = forms.CharField(
        label='کد تخفیف',
        widget=forms.TextInput(attrs={'placeholder': 'کد تخفیف را وارد کنید'})
    )

from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(
                attrs = {
                    'class':'input',
                    'placeholder':'Nome do item',
                    'v-model':'message',
                    '@keyup':'sendOnEnter',
                    'autocomplete': 'off',
                },
            ),
        }
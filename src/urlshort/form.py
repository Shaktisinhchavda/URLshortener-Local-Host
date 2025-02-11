from .models import ShortURL
from django import forms


class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = {'original_url'}

        widgets = {
            'original_website': forms.TextInput(attrs={'class':'form-control'})
            }
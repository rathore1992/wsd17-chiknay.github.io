
from django import forms
from .models import GamesModel
from django.core.exceptions import ValidationError


class GameForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=80)
    description = forms.CharField(required=True, widget=forms.Textarea())
    price = forms.DecimalField(required=True, decimal_places=2, max_digits=9)

    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        if float(self.cleaned_data['price']) < 0:
            raise ValidationError("Price must be positive.")
        return self.cleaned_data['price']

    class Meta:
        model = GamesModel
        fields = ('name', 'description', 'url', 'price', 'logo')
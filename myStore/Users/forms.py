import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class UserRegForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=2, max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Name..'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'user@email.com'}))
    password1 = forms.CharField(required=True, min_length=8, max_length=30, label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput())
    signupAsDeveloper = forms.NullBooleanField(label="Signup as Developer", widget=forms.CheckboxInput(), required=False)

    def clean(self):
        super(UserCreationForm, self).clean()

        # email uniqueness
        if User.objects.filter(email=self.cleaned_data.get('email')).count() > 0:
            raise ValidationError("E-mail already registered")

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'signupAsDeveloper')

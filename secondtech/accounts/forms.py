from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import UserProfile
from common.FormMixin import FormMixin


class RegisterForm(UserCreationForm, FormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data.isalpha():
            raise ValidationError('Please enter a valid First Name')
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not data.isalpha():
            raise ValidationError('Please enter a valid First Name')
        return data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', ]

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if "+359" in str(data):
            if not len(data) == 13:
                raise ValidationError("Please enter a valid phone number")
        elif not len(data) == 10:
            raise ValidationError("Please enter a valid phone number")
        return data


class LoginForm(FormMixin, forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

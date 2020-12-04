from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile
from common.FormMixin import FormMixin


class RegisterForm(UserCreationForm, FormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', ]


class LoginForm(FormMixin, forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

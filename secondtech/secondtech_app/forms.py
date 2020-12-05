from django import forms

from common.FormMixin import FormMixin
from secondtech_app.models import Device


class DeviceForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Device
        exclude = ['user', ]


class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, required=False)

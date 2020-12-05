from django import forms
from django.core.exceptions import ValidationError

from common.FormMixin import FormMixin
from secondtech_app.models import Device


class DeviceForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Device
        exclude = ['user', ]

    def clean_cpu_speed(self):
        data = self.cleaned_data['cpu_speed']
        if data <= 0:
            raise ValidationError('Please enter a valid CPU Speed')
        return data

    def clean_price(self):
        data = self.cleaned_data['price']
        if data <= 0:
            raise ValidationError('Please enter a valid Price')
        return data

    def clean_ram(self):
        data = self.cleaned_data['ram']
        if data <= 0:
            raise ValidationError('Please enter a valid RAM')
        return data

    def clean_storage_capacity(self):
        data = self.cleaned_data['storage_capacity']
        if data <= 0:
            raise ValidationError('Please enter a valid Storage Capacity')
        return data


class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, required=False)

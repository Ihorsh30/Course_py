from django import forms
from .models import DeliveryAddress, Refund


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = DeliveryAddress

        fields = ['user', 'order', 'address', 'city', 'phone']


class RefundForm(forms.ModelForm):
    status = forms.BooleanField()

    class Meta:
        model = Refund

        fields = ['order', 'reason', 'status']

from django import forms
from .models import Order


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['start_date','end_date','coordinator','status','number', 'state','address','client','client_contract','vendor','vendor_sub_out','sub_out']


    def clean(self):
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(NewOrderForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['coordinator'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['client_contract'].widget.attrs['class'] = 'form-control'
        self.fields['vendor'].widget.attrs['class'] = 'form-control'
        self.fields['vendor_sub_out'].widget.attrs['class'] = 'form-control'
        self.fields['sub_out'].widget.attrs['class'] = 'form-control'
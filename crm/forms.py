from django import forms
from crm.models import Common60, Common61, Common70


class ObjectModelForm60(forms.ModelForm):
    class Meta:
        model = Common60
        exclude = '__all__'


class ObjectModelForm61(forms.ModelForm):
    class Meta:
        model = Common61
        exclude = '__all__'


class ObjectModelForm70(forms.ModelForm):
    class Meta:
        model = Common70
        exclude = '__all__'

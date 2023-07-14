from django import forms
from crm.models import Common60


class ObjectModelForm(forms.ModelForm):

    class Meta:
        model = Common60
        exclude = '__all__'

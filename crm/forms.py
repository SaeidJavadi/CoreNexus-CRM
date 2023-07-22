from django import forms
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance


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


class ObjectModelFormCd(forms.ModelForm):
    class Meta:
        model = CommonDead
        exclude = '__all__'


class ObjectModelFormJd(forms.ModelForm):
    class Meta:
        model = JudiciaryDead
        exclude = '__all__'


class ObjectModelFormDd(forms.ModelForm):
    class Meta:
        model = DoingDead
        exclude = '__all__'


class ObjectModelFormPa(forms.ModelForm):
    class Meta:
        model = PublicAssistance
        exclude = '__all__'

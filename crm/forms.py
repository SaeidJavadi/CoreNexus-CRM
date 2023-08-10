from django import forms
from crm.models import Common60, Common61, Common70, CommonDead, JudiciaryDead, DoingDead, PublicAssistance, Notification


class ObjectModelForm60(forms.ModelForm):
    class Meta:
        model = Common60
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelForm60, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelForm61(forms.ModelForm):
    class Meta:
        model = Common61
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelForm61, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelForm70(forms.ModelForm):
    class Meta:
        model = Common70
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelForm70, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelFormCd(forms.ModelForm):
    class Meta:
        model = CommonDead
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelFormCd, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelFormJd(forms.ModelForm):
    class Meta:
        model = JudiciaryDead
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelFormJd, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelFormDd(forms.ModelForm):
    class Meta:
        model = DoingDead
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelFormDd, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelFormPa(forms.ModelForm):
    class Meta:
        model = PublicAssistance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ObjectModelFormPa, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "status":
                visible.field.widget.attrs['class'] = 'form-control'


class ObjectModelFormMSG(forms.ModelForm):
    class Meta:
        model = Notification
        exclude = ('see',)

    def __init__(self, *args, **kwargs):
        super(ObjectModelFormMSG, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class HodlingLotteryForm(forms.Form):
    name = forms.CharField(max_length=150, required=True, label="Lottery Title",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    countwinner = forms.IntegerField(label="Count Winner", widget=forms.NumberInput(
        attrs={'class': 'form-control', type: 'number'}))
    winstatus = forms.BooleanField(label="winners status", required=False)
    agree = forms.BooleanField(label="start holding?")


class AddtoLotteryForm(forms.Form):
    addcount = forms.IntegerField(label='Add to Lottery Count')
    agree = forms.BooleanField(label="agree ?")

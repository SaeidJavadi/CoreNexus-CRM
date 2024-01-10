from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'phone', 'email', 'is_active', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "is_active" and visible.name != "is_staff" and visible.name != "is_superuser":
                visible.field.widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'phone', 'email', 'fcmtoken', 'is_active', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != "is_active" and visible.name != "is_staff" and visible.name != "is_superuser":
                visible.field.widget.attrs['class'] = 'form-control'

    def clean_password(self):
        return self.initial['password']


class ChangePasswordFrom(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Re-Enter Password'}))

    class Meta:
        model = get_user_model()
        fields = ('password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords don\'t match')
        else:
            return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'username', 'name': 'logusername', 'class': 'form-style', 'placeholder': 'Username', 'id': 'logusername', 'autocomplete': 'off'}),)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'logpass', 'class': 'form-style', 'placeholder': 'Password', 'id': 'logpass', 'autocomplete': 'off'}),)


class LoginFormAR(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'username', 'name': 'logusername', 'class': 'form-style', 'placeholder': 'اسم المستخدم', 'id': 'logusername', 'autocomplete': 'off', 'lang': 'ar'}),)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'logpass', 'class': 'form-style', 'placeholder': 'كلمة السر خاصتك', 'id': 'logpass', 'autocomplete': 'off', 'lang': 'ar'}),)

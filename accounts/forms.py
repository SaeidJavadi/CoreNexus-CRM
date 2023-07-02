from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',  'phone', 'is_active', 'is_staff')

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
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username',  'phone', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial['password']


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


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',  'phone')

        widgets = {  # Optional
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel', 'maxlength': '11',
                       'minlength': '11',  'onkeypress': 'return isNumber(event)', 'required': 'false'})}

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


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',  'phone')


class ChangePassword(forms.Form):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Re-Enter Password'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords don\'t match')
        else:
            return password2

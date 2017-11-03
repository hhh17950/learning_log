from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email']




class ChangeForm(forms.Form):
    username = forms.CharField(label='用户名')
    old_password = forms.CharField(label='原密码',widget=forms.PasswordInput())
    new_password_1 = forms.CharField(label='新密码',widget=forms.PasswordInput())
    new_password_2 = forms.CharField(label='请确认密码',widget=forms.PasswordInput())
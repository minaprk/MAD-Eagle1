from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import SimpleUser
#
#
# class SimpleUserForm(UserCreationForm):
#     # password = forms.CharField(widget=forms.PasswordInput())
#     class Meta(UserCreationForm.Meta):
#         model = SimpleUser
#         fields = ('email', 'username', 'userImg')
#
#
# class SimpleUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = SimpleUser
#         fields = ('email', 'username', 'userImg')
from django.contrib.auth.models import User

from appl.models import Customer, Service


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': 'same as your roll no.',
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
            'phone_number']


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['appointment']

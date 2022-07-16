import email
from django import forms
from django.forms import EmailInput, ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'input100','placeholder':'Username','name':'username'})
        self.fields['email'].widget.attrs.update({'class':'input100','placeholder':'Email','name':'email'})
        self.fields['password1'].widget.attrs.update({'class':'input100','placeholder':'Password','name':'password'})        
        self.fields['password2'].widget.attrs.update({'class':'input100','placeholder':'Repeat password','name':'password'})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChangeUserForm(UserChangeForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'input100','placeholder':'Username','name':'username'})
        self.fields['email'].widget.attrs.update({'class':'input100','placeholder':'Email','name':'email'})
        self.fields['password1'].widget.attrs.update({'class':'input100','placeholder':'Password','name':'password'})        
        self.fields['password2'].widget.attrs.update({'class':'input100','placeholder':'Repeat password','name':'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'password', 'password2']

        widgets = {
            'bio': TextInput(attrs={
                'class':'input100',
                'placeholder':'Your bio',
                'name':'bio'
            }),
        }
__author__ = 'Frank'

from django import forms
from django.contrib.auth.models import User
from Main.models import Users

USER_TYPE_CHOICES = (
    ('User', 'User'),
    ('Vendor', 'Vendor'),
)

class BaseUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UsersForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Verify Username")
    #usertype = forms.CharField(max_length=6, help_text="User/Vendor: ")
    usertype = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=USER_TYPE_CHOICES)
    name = forms.CharField(max_length=128)
    birthdate = forms.DateField()
    email = forms.CharField(help_text="Verify Email")


    class Meta:
        model = Users
        #fields = ('userid','usertype','name','birthdate','email','password',)
        fields = ('usertype','name','birthdate','username','email',)

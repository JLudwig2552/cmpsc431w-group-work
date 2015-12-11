__author__ = 'Frank'

from django import forms
from Main.models import User

USER_TYPE_CHOICES = (
    ('User', 'User'),
    ('Vendor', 'Vendor'),
)

class UsersForm(forms.ModelForm):
    userid = forms.CharField(max_length=128, help_text="Username: ")
    #usertype = forms.CharField(max_length=6, help_text="User/Vendor: ")
    usertype = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=USER_TYPE_CHOICES)
    name = forms.CharField(max_length=128, help_text="Name: ")
    birthdate = forms.DateField(help_text="Date of Birth: ")
    email = forms.CharField(help_text="Email: ")

    class Meta:
        model = User
        fields = ('userid','usertype','name','birthdate','email',)

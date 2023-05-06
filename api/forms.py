

from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class UserBulkUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

# C:\Users\Asus\Desktop


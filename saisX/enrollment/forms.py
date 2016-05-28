from django import forms
from django.contrib.auth import authenticate
from .models import Student
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=3, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user =  authenticate(username=username, password=password)
        print user
        if user:
            cleaned_data['user'] = user
        else:
            raise forms.ValidationError(
                'Username/Password is incorrect.'
            )
        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['contact_number', 'email', 'mother_contact', 'father_contact', 'current_address', 'home_address']

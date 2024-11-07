from django import forms
from .models import *
class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields='__all__'
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError("Username should not contain any spaces.")
        return username        
    def clean(self):
        cleaned_data=super().clean()
        print('fullform',cleaned_data)
        return cleaned_data
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password !=confirm_password:
            raise forms.ValidationError("password and confirm pass not matched")
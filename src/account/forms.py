from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    first_name = forms.CharField(max_length=60, help_text='Required. Add a valid first name')
    last_name = forms.CharField(max_length=60, help_text='Required. Add a valid last name')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')
            
            
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')
    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)
        
    def clean_full_name(self):
        if self.is_valid():
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(first_name=first_name, last_name=last_name)
            except Account.DoesNotExist:
                return first_name, last_name
            
            raise forms.ValidationError('Name "%s %s" is already in use.' % (account.first_name, account.last_name))
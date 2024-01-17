from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, max_length=60, help_text='Required. Add a valid email address')
    first_name = forms.CharField(required = True, max_length=60, help_text='Required. Add a valid first name')
    last_name = forms.CharField(required = True, max_length=60, help_text='Required. Add a valid last name')
    job_title = forms.CharField(required = True, max_length=60, help_text='Required. Add a valid job title')
    company = forms.CharField(required = True, max_length=60, help_text='Required. Add a valid company')
    phone_number = forms.CharField(required = True, max_length=60, help_text='Required. Add a valid phone number')
    password1 = forms.CharField(required = True, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(required = True, label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'job_title', 'company', 'phone_number', 'password1', 'password2')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)
    
    def save(self, commit=True):
        account = super(RegistrationForm, self).save(commit=False)
        account.email = self.cleaned_data['email']
        account.first_name = self.cleaned_data['first_name']
        account.last_name = self.cleaned_data['last_name']
        account.job_title = self.cleaned_data['job_title']
        account.company = self.cleaned_data['company']
        account.phone_number = self.cleaned_data['phone_number']
        account.set_password(self.cleaned_data['password1'])
        if commit:
            account.save()
        return account


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
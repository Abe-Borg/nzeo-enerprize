from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True, label="Confirm email")

    class Meta:
        model = User
        fields = ("username", "email", "confirm_email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['confirm_email'].widget.attrs.update({'placeholder': 'Confirm Email'})

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error('confirm_email', "Emails must match")

        return cleaned_data
    


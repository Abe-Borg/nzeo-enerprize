from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from district_management.models import SchoolDistrict
from django.db import transaction
from district_management.models import SchoolDistrict
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True, label="Confirm email")
    user_district = forms.ModelChoiceField(queryset=SchoolDistrict.objects.all(), required=True, empty_label="Select District")
    user_school = forms.ModelChoiceField(queryset=School.objects.none(), required=False)  # Initially empty
    job_title = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "confirm_email", "password1", "password2", "user_district", "user_school", "job_title")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['confirm_email'].widget.attrs.update({'placeholder': 'Confirm Email'})
        
        # Dynamically load user_school queryset based on user_district if in POST data
        if 'user_district' in self.data:
            try:
                district_id = int(self.data.get('user_district'))
                self.fields['user_school'].queryset = School.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # Invalid input; fallback to empty School queryset


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error('confirm_email', "Emails must match")

        return cleaned_data


    def save(self, commit=True):
        with transaction.atomic():
            user = super().save(commit=False)
            if commit:
                user.save()
                user_profile = UserProfile.objects.create(
                    user=user,
                    user_district=self.cleaned_data.get('user_district'),
                    user_school=self.cleaned_data.get('user_school'),
                    job_title=self.cleaned_data.get('job_title'),
                )
        return user
    

class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
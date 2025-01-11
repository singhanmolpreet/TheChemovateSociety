from django import forms
from .models import CustomUser, CandidateProfile, CompanyProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'role', 'password']

class CandidateExtraForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['experience', 'expertise', 'image']

class CompanyExtraForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'address', 'description', 'image', 'gstin']

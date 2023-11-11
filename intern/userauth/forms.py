from django import forms
from .models import Patient, Doctor

class PatientSignUpForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(), 'confirm_password': forms.PasswordInput()}

class DoctorSignUpForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(), 'confirm_password': forms.PasswordInput()}

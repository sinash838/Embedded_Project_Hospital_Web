from django import forms

from .models import HospitalBed, Patient


class HospitalBedPatientForm(forms.ModelForm):
    class Meta:
        model = HospitalBed
        fields = ['occupied_patient']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']

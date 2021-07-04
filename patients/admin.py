from django.contrib import admin

# Register your models here.
from patients.models import Patient, HospitalBed

admin.site.register(Patient)
admin.site.register(HospitalBed)

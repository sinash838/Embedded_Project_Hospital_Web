from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse

from patients.forms import HospitalBedPatientForm, PatientForm
from patients.models import HospitalBed


@login_required
def hospital_beds_list_view(request):
    beds = HospitalBed.objects.all()
    return render(request,
                  'patients/hospital_bed_list.html',
                  {
                      'auth': True,
                      'beds': beds,
                  })


@login_required
def hospital_bed_profile_view(request, bed_id):
    bed = get_object_or_404(HospitalBed, pk=bed_id)
    return render(request,
                  'patients/hospital_bed_profile.html',
                  {
                      'bed': bed,
                  })


@login_required
def create_patient(request):
    form = PatientForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()

            return HttpResponseRedirect(reverse('patients:beds_list'))
    return render(request,
                  'patients/patient_create.html', {
                      'form': form,
                  })


@login_required
def edit_hospital_bed_view(request, bed_id):
    bed = get_object_or_404(HospitalBed, pk=bed_id)
    form = HospitalBedPatientForm(request.POST or None, instance=bed)
    if request.method == 'POST':
        if form.is_valid():
            hospital_bed = form.save()
            return HttpResponseRedirect(reverse('patients:bed_view',
                                                args=(hospital_bed.id,)))
    return render(request,
                  'patients/hospital_bed_patient_edit.html',
                  {
                      'form': form,
                      'bed': bed,
                  })


def update_patient_status(request, bed_id, temp, sbp, dbp, bo, pulse):
    bed = get_object_or_404(HospitalBed, pk=bed_id)
    bed.measured_temperature = temp
    bed.measured_sbp = sbp
    bed.measured_dbp = dbp
    bed.measured_heart_rate = pulse
    bed.measured_oxygen_level = bo
    bed.save()
    return {"status": "ok"}

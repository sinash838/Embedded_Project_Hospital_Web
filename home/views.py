from django.shortcuts import render

from patients.models import Patient, HospitalBed


def home_page(request):
    """View function for home page of site."""

    user_cnt = Patient.objects.filter().count()
    bed_cnt = HospitalBed.objects.filter().count()

    context = {
        'patient_cnt': user_cnt,
        'bed_cnt': bed_cnt,
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home/home.html', context=context)

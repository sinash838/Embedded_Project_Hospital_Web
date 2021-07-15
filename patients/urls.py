from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.hospital_beds_list_view, name='beds_list'),
    path('<int:bed_id>/', views.hospital_bed_profile_view, name='bed_view'),
    path('<int:bed_id>/edit/', views.edit_hospital_bed_view, name='bed_edit'),
    path('create/', views.create_patient, name='patient_create'),
    path('update_status/<int:bed_id><int:temp><int:sbp><int:dbp><int:bo><int:pulse>/', views.update_patient_status, name='update_status'),
]

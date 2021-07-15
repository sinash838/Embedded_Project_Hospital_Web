from django.db import models


# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False, default="")
    last_name = models.CharField(max_length=200, blank=False, null=False, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name


class HospitalBed(models.Model):
    occupied_patient = models.OneToOneField(Patient, null=True, blank=True, on_delete=models.DO_NOTHING)
    measured_temperature = models.IntegerField(null=False, default=37)
    measured_sbp = models.IntegerField(null=False, default=120)
    measured_dbp = models.IntegerField(null=False, default=80)
    measured_oxygen_level = models.IntegerField(null=False, default=87)
    measured_heart_rate = models.IntegerField(null=False, default=80)

    def __str__(self):
        if self.occupied_patient is None:
            return "Empty Bed"
        return str(self.occupied_patient)

    @property
    def alert_status(self):
        if self.occupied_patient is None:
            return False
        if not (36.5 < self.measured_temperature < 37.5) or not (110 < self.measured_sbp < 120) or not (
                75 < self.measured_sbp < 90) or not (
                95 < self.measured_oxygen_level < 100) or not (60 < self.measured_heart_rate < 100):
            return True
        return False

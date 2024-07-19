from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default='')
    place_of_birth = models.CharField(max_length=100, default='')
    sex = models.CharField(max_length=10, default='')
    civil_status = models.CharField(max_length=20, default='')
    height = models.FloatField(default=1.70)
    weight = models.FloatField(default=70.0)
    blood_type = models.CharField(max_length=3, default='')
    gsis_id_no = models.CharField(max_length=20, default='')
    pagibig_id_no = models.CharField(max_length=20, default='')
    philhealth_no = models.CharField(max_length=20, default='')
    sss_no = models.CharField(max_length=20, default='')
    tin_no = models.CharField(max_length=20, default='')
    agency_employee_no = models.CharField(max_length=20, default='')
    citizenship = models.CharField(max_length=50, default='')
    residential_address = models.CharField(max_length=255, default='')
    zip_code = models.CharField(max_length=10, default='')
    permanent_address = models.CharField(max_length=255, default='')
    telephone_no = models.CharField(max_length=20, default='')
    mobile_no = models.CharField(max_length=20, default='')
    email_address = models.EmailField(default='')
    fathers_name = models.CharField(max_length=100, default='')
    mothers_name = models.CharField(max_length=100, default='')

    def str(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"
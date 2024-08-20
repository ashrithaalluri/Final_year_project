from django.db import models

# Create your models here.
class specialization_details(models.Model):
    sp_name=models.CharField(max_length=100)
    sp_discription=models.CharField(max_length=200)

    def __str__(self):
        return self.sp_name
    

class doctor_details(models.Model):
    dr_name=models.CharField(max_length=200)
    dr_contact=models.CharField(max_length=15)
    dr_specialization=models.ForeignKey(specialization_details,on_delete=models.CASCADE)
    dr_photo=models.FileField(upload_to="drimages/",max_length=250,null=True,default=None)
    dr_qualification=models.CharField(max_length=200)
    dr_experince=models.CharField(max_length=200)
    def __str__(self):
        return self.dr_name
    @property
    def sp_name(self):
        return self.dr_specialization.sp_name



class patient_details(models.Model):
    patient_name=models.CharField(max_length=100)
    patient_contact=models.CharField(max_length=100)
    patient_email=models.CharField(max_length=100)
    patient_address=models.CharField(max_length=100)
    patient_photo=models.FileField(upload_to="drimages/",max_length=250,null=True,default=None)
    pswrd=models.CharField(max_length=100) 
    def __str__(self):
        return self.patient_name
    

class appoinmentscheduel(models.Model):
    doctor_id=models.ForeignKey(doctor_details,on_delete=models.CASCADE)
    appoinment_day=models.CharField(max_length=200)
    hours_minutes=models.CharField(max_length=200, default="")
    appoinment_status=models.CharField(max_length=100)

class appointement_req(models.Model):
    doctor_id=models.ForeignKey(doctor_details,on_delete=models.CASCADE)
    appoinment_day=models.CharField(max_length=200)
    hours_minutes=models.CharField(max_length=200, default="")
    patient_id=models.ForeignKey(patient_details,on_delete=models.CASCADE)
    appoinment_status=models.CharField(max_length=100) 

class patient_reports(models.Model):
    patient_id=models.ForeignKey(patient_details,on_delete=models.CASCADE)
    patient_report_name=models.CharField(max_length=200)
    report_file=models.CharField(max_length=200)
    report_date=models.CharField(max_length=100)
    refferd_by=models.ForeignKey(doctor_details,on_delete=models.CASCADE)

class VideoChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)




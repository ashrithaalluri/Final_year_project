from django.contrib import admin
from .models import *

# Register your models here.
class specialization(admin.ModelAdmin):
    list_display=('id','sp_name','sp_discription')
admin.site.register(specialization_details,specialization)

class doctor(admin.ModelAdmin):
    list_display=('id','dr_name','dr_contact','dr_specialization','dr_photo','dr_qualification','dr_experince')
admin.site.register(doctor_details,doctor)

class patient(admin.ModelAdmin):
    list_display=('id','patient_name','patient_contact','patient_email','patient_address','patient_photo','pswrd')
admin.site.register(patient_details,patient)

class appoinments(admin.ModelAdmin):
    list_display=('id','doctor_id','appoinment_day','hours_minutes','appoinment_status')
admin.site.register(appoinmentscheduel,appoinments)

class patient_r(admin.ModelAdmin):
    list_display=('id','patient_id','patient_report_name','report_file','report_date','refferd_by')
admin.site.register(patient_reports,patient_r)
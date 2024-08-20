from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
   path("adminhome/",adminhome),
   path("video_conference/",video_conference),
   path("userhome/",userhome),
   path("specializationform/",specializationform),
   path("specializationview/",specializationview),
   path("specializationdelete/<int:sp_id>",specializationdelete),
   path("specializationedit/<int:sp_id>",specializationedit),
   path("specializationupdate/<int:sp_id>",specializationupdate),


   path("doctordetailsform/",doctordetailsform),
   path("doctordetailsview/",doctordetailsview),
   path("doctordetailsdelete/<int:d_id>",doctordetailsdelete),
   path("doctordetailsedit/",doctordetailsedit),
   path("doctordetailsupdate/<int:d_id>",doctordetailsupdate),



   path("appoinmentscheduelform/",appoinmentscheduelform),
   path("appoinmentscheduelview/",appoinmentscheduelview),
   path("appoinmentschedueldelete/<int:d_id>",appoinmentschedueldelete),
   path("appoinmentschedueledit/<int:d_id>",appoinmentschedueledit),
   path("appoinmentscheduelupdate/<int:d_id>",appoinmentscheduelupdate),
   path("userappoinmentscheduelview/",userappoinmentscheduelview),
   path("userappoinmentschedueledit/<int:d_id>",userappoinmentschedueledit),
   path("bookappoinment/<int:sid>",bookappoinment),
   path("appoinmentstatusview/",appoinmentstatusview),





   path("patientdetailsform/",patientdetailsform),
   path("patientdetailsview/",patientdetailsview),
   path("patientdetailsdelete/<int:p_id>",patientdetailsdelete),
   path("patientdetailsedit/",patientdetailsedit),
   path("patientdetailsupdate/<int:p_id>",patientdetailsupdate),
   path("userpatientreportview/", userpatientreportview),


   
   path("patientreportform/",patientreportform),
   path("patientreportview/",patientreportview),
   path("patientreportdelete/<int:ref_id>",patientreportdelete),
   path("patientreportedit/<int:ref_id>",patientreportedit),
   path("patientreportupdate/<int:ref_id>",patientreportupdate),


]

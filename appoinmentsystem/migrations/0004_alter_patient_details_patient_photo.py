# Generated by Django 4.2.3 on 2023-09-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appoinmentsystem", "0003_alter_doctor_details_dr_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient_details",
            name="patient_photo",
            field=models.FileField(
                default=None, max_length=250, null=True, upload_to="drimages/"
            ),
        ),
    ]

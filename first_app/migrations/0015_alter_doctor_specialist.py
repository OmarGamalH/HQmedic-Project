# Generated by Django 5.1.1 on 2024-11-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_doctor_age_doctor_gender_patient_age_patient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialist',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
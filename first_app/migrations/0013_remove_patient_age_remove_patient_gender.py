# Generated by Django 5.1.1 on 2024-10-30 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0012_alter_patient_user_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
    ]

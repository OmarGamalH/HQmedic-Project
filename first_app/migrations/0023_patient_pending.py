# Generated by Django 5.1.3 on 2024-11-18 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0022_doctors_advices'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_pending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctors', models.ManyToManyField(related_name='doctor_pendings', to='first_app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_pendings', to='first_app.patient')),
            ],
        ),
    ]

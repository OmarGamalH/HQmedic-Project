# Generated by Django 5.1.1 on 2024-11-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0018_remove_doctor_age_remove_doctor_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(default='None', max_length=20),
        ),
    ]

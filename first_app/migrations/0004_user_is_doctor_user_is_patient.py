# Generated by Django 5.1.1 on 2024-10-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_user_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]

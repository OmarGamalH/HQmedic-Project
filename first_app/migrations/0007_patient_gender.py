# Generated by Django 5.1.1 on 2024-10-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=65, null=True),
        ),
    ]
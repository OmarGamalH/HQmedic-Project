# Generated by Django 5.1.1 on 2024-10-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Category',
            field=models.CharField(max_length=65, null=True),
        ),
    ]

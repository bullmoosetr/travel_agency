# Generated by Django 3.1.5 on 2021-01-25 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0023_auto_20210125_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinationtype',
            old_name='danger_level',
            new_name='destinations',
        ),
    ]
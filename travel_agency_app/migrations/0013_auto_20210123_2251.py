# Generated by Django 3.1.5 on 2021-01-23 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0012_location_is_a_capital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='is_a_capital',
            new_name='is_capital',
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0049_auto_20210127_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='availability',
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0017_auto_20210125_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='tour_package',
        ),
        migrations.AddField(
            model_name='tourpackage',
            name='tour_package',
            field=models.ManyToManyField(to='travel_agency_app.Destination'),
        ),
    ]

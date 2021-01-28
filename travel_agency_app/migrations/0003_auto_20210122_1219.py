# Generated by Django 3.1.5 on 2021-01-22 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0002_auto_20210122_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geolocation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='geo_location',
        ),
        migrations.AddField(
            model_name='geolocation',
            name='location',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='travel_agency_app.location'),
            preserve_default=False,
        ),
    ]
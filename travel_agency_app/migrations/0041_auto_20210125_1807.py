# Generated by Django 3.1.5 on 2021-01-25 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0040_auto_20210125_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='travel_agency_app.location'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-25 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_delete_services'),
        ('users', '0007_auto_20210125_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.servicedetails'),
        ),
    ]

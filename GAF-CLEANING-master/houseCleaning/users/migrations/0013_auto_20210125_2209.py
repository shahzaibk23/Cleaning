# Generated by Django 3.1.5 on 2021-01-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_booking_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.employee2'),
        ),
    ]

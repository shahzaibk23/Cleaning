# Generated by Django 3.1.5 on 2021-01-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210125_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='profit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

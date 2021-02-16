# Generated by Django 3.1.5 on 2021-01-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('full_address', models.CharField(max_length=80)),
                ('postcode', models.CharField(max_length=20)),
                ('tel_number', models.CharField(max_length=20)),
                ('mob_number', models.CharField(max_length=20)),
                ('next_of_kin', models.CharField(max_length=50)),
                ('training_levels', models.CharField(max_length=20)),
                ('site_stationed', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('line_supervisor', models.CharField(max_length=40)),
                ('line_manager', models.CharField(max_length=60)),
            ],
        ),
    ]

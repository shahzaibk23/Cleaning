# Generated by Django 3.1.5 on 2021-02-18 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_suppliers'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_address', models.CharField(max_length=100)),
                ('property_type', models.CharField(max_length=100)),
                ('property_size', models.CharField(max_length=100)),
                ('floor_area_size', models.CharField(max_length=100)),
                ('floor_plan', models.CharField(max_length=100)),
                ('floor_type', models.CharField(max_length=100)),
                ('contract_type', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('cleaning_requirements', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, max_length=1000, null=True)),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
        ),
    ]

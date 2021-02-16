# Generated by Django 3.1.5 on 2021-01-20 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210120_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='hourlyRate',
        ),
        migrations.AddField(
            model_name='hourlyrate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.panel'),
        ),
    ]
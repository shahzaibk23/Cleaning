# Generated by Django 3.1.5 on 2021-02-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20210221_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_address', models.CharField(max_length=100)),
                ('business_information', models.CharField(max_length=100)),
                ('customer_information', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_reference', models.CharField(max_length=100)),
                ('po_no', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=100)),
                ('notes', models.TextField(max_length=1000)),
                ('due_date', models.CharField(max_length=100)),
                ('company_number', models.CharField(max_length=100)),
                ('vat_number', models.CharField(max_length=100)),
                ('bank_account_no', models.CharField(max_length=100)),
                ('sort_code_no', models.CharField(max_length=100)),
                ('notes_and_attachments', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productivity_report', models.CharField(max_length=100)),
                ('job_report', models.CharField(max_length=100)),
                ('time_sheet_report', models.CharField(max_length=100)),
                ('job_financial_report', models.CharField(max_length=100)),
                ('quote_create', models.CharField(max_length=100)),
                ('quote_expired', models.CharField(max_length=100)),
                ('quote_converted_bad_debts', models.CharField(max_length=100)),
                ('aged_recievables', models.CharField(max_length=100)),
                ('one_of_jobs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobs', models.CharField(max_length=100)),
                ('start_date_and_time', models.CharField(max_length=100)),
                ('end_date_and_time', models.CharField(max_length=100)),
                ('staff', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('schedule_calender', models.CharField(max_length=100)),
                ('colorCode', models.CharField(choices=[('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN')], max_length=100)),
            ],
        ),
    ]

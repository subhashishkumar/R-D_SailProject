# Generated by Django 2.0.5 on 2018-05-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllAccident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50, verbose_name='Unit Name')),
                ('emp_id', models.CharField(max_length=15, verbose_name='Employee ID')),
                ('emp_type', models.CharField(choices=[('Regular', 'Regular'), ('Contract', 'Contract')], default='Regular', max_length=20, verbose_name='Employee Type')),
                ('emp_name', models.CharField(max_length=30, verbose_name='Employee Name')),
                ('age', models.PositiveSmallIntegerField(default='21', verbose_name='Age')),
                ('dept', models.CharField(max_length=50, verbose_name='Department')),
                ('shift', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('G', 'G')], default='A', max_length=5, verbose_name='Shift')),
                ('accd_type', models.CharField(choices=[('Fatal', 'Fatal'), ('Reportable', 'Reportable'), ('Non-Reportable', 'Non-Reportable'), ('First-Aid', 'First-Aid')], default='Fatal', max_length=30, verbose_name='Accident Type')),
                ('date', models.DateTimeField(verbose_name='Date and Time')),
                ('cause', models.CharField(choices=[('Common Causes:', (('Fall of material', 'Fall of material'), ('Material handling', 'Material handling'), ('Road incident', 'Road incident'), ('Slip', 'Slip'), ('Fall of person', 'Fall of person'), ('Burn', 'Burn'), ('Electrocution', 'Electrocution'), ('Gas exposure', 'Gas exposure'), ('Hit/Caught/Pressed', 'Hit/Caught/Pressed'))), ('Others:', (('Violation of SOPs', 'Violation of SOPs'), ('Violation of SMPs', 'Violation of SMPs'), ('BBS Aspects', 'BBS Aspects'), ('Equipment Failure', 'Equipment Failure')))], default='Slip', max_length=100, verbose_name='Accident Cause')),
                ('narrative', models.TextField(verbose_name='Narrative')),
                ('learning_point', models.CharField(blank=True, max_length=100, verbose_name='Learning Point')),
            ],
            options={
                'verbose_name_plural': 'Accident Details',
            },
        ),
        migrations.CreateModel(
            name='Manhours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=30, verbose_name='Unit Name')),
                ('date', models.DateField(verbose_name='Date')),
                ('manhours_worked_regular', models.BigIntegerField(default=0, verbose_name='Manhours Worked Regular')),
                ('manhours_worked_contract', models.BigIntegerField(default=0, verbose_name='Manhours Worked Contract')),
                ('mandays_lost', models.IntegerField(verbose_name='Man-Days Lost')),
            ],
            options={
                'verbose_name_plural': 'Manhours Details',
            },
        ),
    ]
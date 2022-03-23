# Generated by Django 4.0.1 on 2022-03-07 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hr', '0023_organization1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personalinfo',
            fields=[
                ('firstname', models.CharField(db_column='FirstName', max_length=10, primary_key=True, serialize=False)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=10, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=10, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('intial', models.CharField(blank=True, db_column='Intial', max_length=5, null=True)),
                ('maritalstatus', models.CharField(blank=True, db_column='MaritalStatus', max_length=10, null=True)),
                ('ethnicitycode', models.CharField(blank=True, db_column='EthnicityCode', max_length=10, null=True)),
                ('iseffective', models.IntegerField(blank=True, db_column='IsEffective', null=True)),
                ('effectivestartdate', models.DateField(blank=True, db_column='EffectiveStartDate', null=True)),
                ('effectiveenddate', models.DateField(blank=True, db_column='EffectiveEndDate', null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
    ]

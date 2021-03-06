# Generated by Django 4.0.1 on 2022-03-07 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hr', '0019_jobinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaveinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, db_column='Year', max_length=10, null=True)),
                ('leavebalance', models.IntegerField(blank=True, db_column='LeaveBalance', null=True)),
                ('leavesavailed', models.IntegerField(blank=True, db_column='LeavesAvailed', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
    ]

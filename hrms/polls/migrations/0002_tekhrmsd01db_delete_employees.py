# Generated by Django 4.0.1 on 2022-01-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tekhrmsd01db',
            fields=[
                ('Emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.TextField(max_length=1000)),
                ('Last_name', models.TextField(max_length=1000)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tekhrmsd01db',
            },
        ),
        migrations.DeleteModel(
            name='employees',
        ),
    ]

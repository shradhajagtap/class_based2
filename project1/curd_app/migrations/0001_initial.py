# Generated by Django 5.0.3 on 2024-04-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_company_name', models.CharField(max_length=10)),
                ('emp_first_name', models.CharField(max_length=20)),
                ('emp_last_name', models.CharField(max_length=20)),
                ('emp_id', models.IntegerField()),
                ('emp_city', models.CharField(max_length=10)),
            ],
        ),
    ]

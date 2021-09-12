# Generated by Django 3.2.7 on 2021-09-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=60)),
                ('mileage', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60)),
                ('day', models.DateField()),
            ],
        ),
    ]
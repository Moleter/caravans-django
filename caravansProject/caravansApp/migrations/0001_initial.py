# Generated by Django 5.0.6 on 2024-11-02 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caravan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('seating', models.CharField(max_length=63, verbose_name='Seatings')),
                ('transmission', models.CharField(max_length=63, verbose_name='transmission')),
                ('year_of_production', models.IntegerField(verbose_name='year')),
            ],
        ),
        migrations.CreateModel(
            name='MessageForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('email', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('message', models.CharField(max_length=511, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(verbose_name='Data początkowa')),
                ('endDate', models.DateField(verbose_name='Data końcowa')),
                ('caravan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caravansApp.caravan')),
            ],
        ),
        migrations.CreateModel(
            name='CaravanImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='Image')),
                ('caravan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caravansApp.caravan')),
            ],
        ),
    ]

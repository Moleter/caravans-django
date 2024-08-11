# Generated by Django 5.0.6 on 2024-08-11 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caravansApp', '0007_alter_messageform_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='date',
        ),
        migrations.AddField(
            model_name='calendar',
            name='caravan',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='caravansApp.caravan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calendar',
            name='endDate',
            field=models.DateField(default=None, verbose_name='Data końcowa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calendar',
            name='startDate',
            field=models.DateField(default=None, verbose_name='Data początkowa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messageform',
            name='name',
            field=models.CharField(max_length=254, verbose_name='Name'),
        ),
    ]
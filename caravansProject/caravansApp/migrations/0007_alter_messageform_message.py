# Generated by Django 5.0.6 on 2024-08-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caravansApp', '0006_messageform_delete_massageform_alter_calendar_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageform',
            name='message',
            field=models.CharField(max_length=511, verbose_name='Message'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-30 11:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_contactus_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
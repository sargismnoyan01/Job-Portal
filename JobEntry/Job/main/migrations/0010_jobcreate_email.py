# Generated by Django 4.2.4 on 2023-08-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_jobcreate_about_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcreate',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
    ]
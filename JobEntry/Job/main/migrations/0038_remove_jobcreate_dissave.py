# Generated by Django 4.2.4 on 2023-09-27 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_jobcreate_dissave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcreate',
            name='dissave',
        ),
    ]

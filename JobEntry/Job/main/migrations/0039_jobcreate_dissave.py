# Generated by Django 4.2.4 on 2023-09-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_remove_jobcreate_dissave'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcreate',
            name='dissave',
            field=models.BooleanField(default=False),
        ),
    ]
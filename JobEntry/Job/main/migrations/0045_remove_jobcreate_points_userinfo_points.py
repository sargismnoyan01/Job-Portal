# Generated by Django 4.2.4 on 2023-12-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_jobcreate_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcreate',
            name='points',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='points',
            field=models.IntegerField(default=10),
        ),
    ]

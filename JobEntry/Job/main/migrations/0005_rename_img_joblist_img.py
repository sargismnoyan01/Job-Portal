# Generated by Django 4.2.4 on 2023-08-14 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_joblist_jobtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joblist',
            old_name='Img',
            new_name='img',
        ),
    ]

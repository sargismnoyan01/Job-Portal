# Generated by Django 4.2.4 on 2023-08-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_jobcreate_discription_jobcreate_qualifications_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcreate',
            name='about_company',
            field=models.TextField(blank=True, verbose_name='Company Detail'),
        ),
    ]

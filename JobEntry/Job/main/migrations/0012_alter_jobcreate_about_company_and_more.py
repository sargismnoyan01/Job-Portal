# Generated by Django 4.2.4 on 2023-08-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_homeabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcreate',
            name='about_company',
            field=models.TextField(null=True, verbose_name='Company Detail'),
        ),
        migrations.AlterField(
            model_name='jobcreate',
            name='discription',
            field=models.TextField(null=True, verbose_name='Job description'),
        ),
        migrations.AlterField(
            model_name='jobcreate',
            name='qualifications',
            field=models.TextField(null=True, verbose_name='Qualifications'),
        ),
        migrations.AlterField(
            model_name='jobcreate',
            name='responsibility',
            field=models.TextField(null=True, verbose_name='Responsibility'),
        ),
    ]
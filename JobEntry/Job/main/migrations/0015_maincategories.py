# Generated by Django 4.2.4 on 2023-08-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_ourcleints'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255, verbose_name='icon')),
                ('category', models.CharField(max_length=60, verbose_name='Category')),
            ],
        ),
    ]

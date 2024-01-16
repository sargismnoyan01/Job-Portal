# Generated by Django 4.2.1 on 2023-06-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_panel_producttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='index_images', verbose_name='Home logo')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Home logo date')),
            ],
        ),
    ]

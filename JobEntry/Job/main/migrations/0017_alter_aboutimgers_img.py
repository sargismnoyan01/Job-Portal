# Generated by Django 4.2.4 on 2023-08-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_aboutimgers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutimgers',
            name='img',
            field=models.ImageField(upload_to='About_media', verbose_name='Imagers'),
        ),
    ]

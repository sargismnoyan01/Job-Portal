# Generated by Django 4.2.4 on 2023-12-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_remove_apply_portfolio_apply_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeabout',
            name='img',
            field=models.ImageField(null=True, upload_to='Home_media'),
        ),
    ]

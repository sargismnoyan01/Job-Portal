# Generated by Django 4.2.4 on 2023-08-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_talent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
    ]

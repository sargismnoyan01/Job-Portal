# Generated by Django 4.2.4 on 2023-08-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_jobcreate_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(verbose_name='text')),
            ],
        ),
    ]

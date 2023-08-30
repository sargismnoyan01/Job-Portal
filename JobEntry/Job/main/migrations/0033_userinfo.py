# Generated by Django 4.2.4 on 2023-08-30 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0032_alter_contactus_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='users', verbose_name='imagers')),
                ('prof', models.CharField(max_length=255, verbose_name='profession')),
                ('about', models.TextField(blank=True, verbose_name='about')),
                ('education', models.CharField(blank=True, max_length=255, verbose_name='Education')),
                ('licenses', models.CharField(blank=True, max_length=255, verbose_name='Licenses & certificationsLicenses')),
                ('skills', models.CharField(blank=True, max_length=500, verbose_name='skills')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userp', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Info',
                'verbose_name_plural': 'Users info',
            },
        ),
    ]
# Generated by Django 2.2 on 2020-12-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringToken',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authtoken.token',),
        ),
    ]
# Generated by Django 2.2 on 2021-03-06 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0025_buyrequest_approve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyrequest',
            name='approve',
        ),
    ]

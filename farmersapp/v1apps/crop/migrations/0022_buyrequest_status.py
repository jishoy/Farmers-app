# Generated by Django 2.2 on 2021-03-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0021_buyrequest_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]

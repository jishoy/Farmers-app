# Generated by Django 2.2 on 2021-01-11 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0006_auto_20210111_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyrequest',
            name='total_amt',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]

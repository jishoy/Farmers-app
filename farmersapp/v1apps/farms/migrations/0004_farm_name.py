# Generated by Django 2.2 on 2021-03-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_auto_20210304_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='name'),
        ),
    ]

# Generated by Django 2.2 on 2021-03-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0020_auto_20210305_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyrequest',
            name='title',
            field=models.CharField(default=None, max_length=30, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
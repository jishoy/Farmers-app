# Generated by Django 2.2 on 2021-03-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0016_remove_cropactivity_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropactivity',
            name='date',
            field=models.DateField(blank=True, default=None, verbose_name='Date'),
            preserve_default=False,
        ),
    ]

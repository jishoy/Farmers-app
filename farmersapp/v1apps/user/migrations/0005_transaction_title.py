# Generated by Django 2.2 on 2021-03-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_transaction_font_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='title',
            field=models.CharField(default=None, max_length=30, verbose_name='Title'),
            preserve_default=False,
        ),
    ]

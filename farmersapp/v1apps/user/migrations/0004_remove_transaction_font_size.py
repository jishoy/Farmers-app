# Generated by Django 2.2 on 2021-03-03 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_transaction_font_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='font_size',
        ),
    ]
# Generated by Django 2.2 on 2021-03-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0017_cropactivity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='fertilizer_expense',
            field=models.IntegerField(verbose_name='Fertilizer Expense'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='machine_expense',
            field=models.IntegerField(verbose_name='Machine Expense'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='seed_expense',
            field=models.IntegerField(verbose_name='Seed Expense'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='total_expense',
            field=models.IntegerField(verbose_name='Total Expense'),
        ),
    ]

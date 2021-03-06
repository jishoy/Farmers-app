# Generated by Django 2.2 on 2021-03-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0008_auto_20210305_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=30, verbose_name='area')),
            ],
        ),
        migrations.CreateModel(
            name='Vilage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='name')),
            ],
        ),
    ]

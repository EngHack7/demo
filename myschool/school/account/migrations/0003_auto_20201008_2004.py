# Generated by Django 3.0.5 on 2020-10-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201007_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='the_id_number',
            field=models.IntegerField(unique=True, verbose_name='the_id_number'),
        ),
    ]

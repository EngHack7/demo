# Generated by Django 3.0.5 on 2020-10-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201008_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='the_id_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='the_id_number'),
        ),
    ]

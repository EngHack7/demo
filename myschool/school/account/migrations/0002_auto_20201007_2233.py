# Generated by Django 3.0.5 on 2020-10-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachernotes',
            name='teacher_id',
            field=models.IntegerField(),
        ),
    ]

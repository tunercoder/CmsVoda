# Generated by Django 4.1 on 2022-09-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='msisdn',
            field=models.BigIntegerField(),
        ),
    ]

# Generated by Django 3.2 on 2021-06-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20210526_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data_time',
            field=models.DateField(auto_now=True, verbose_name='Время'),
        ),
    ]

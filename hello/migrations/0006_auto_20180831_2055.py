# Generated by Django 2.1.1 on 2018-08-31 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20180831_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

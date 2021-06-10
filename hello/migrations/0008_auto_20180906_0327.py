# Generated by Django 2.1.1 on 2018-09-06 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20180906_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shifts', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-15 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rafinhas', '0008_auto_20190715_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financas',
            name='data',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
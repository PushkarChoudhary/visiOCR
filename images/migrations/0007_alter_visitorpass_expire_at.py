# Generated by Django 5.1.2 on 2024-11-14 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_alter_visitorpass_expire_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorpass',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 14, 16, 54, 18, 755086, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_visitorpass_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorpass',
            name='duration',
            field=models.TimeField(max_length=5),
        ),
    ]
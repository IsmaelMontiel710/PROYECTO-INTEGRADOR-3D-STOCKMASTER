# Generated by Django 4.2.5 on 2023-10-01 01:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0008_alter_mensajes_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='tiempo_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
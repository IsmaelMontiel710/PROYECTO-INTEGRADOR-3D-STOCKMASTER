# Generated by Django 4.2.5 on 2023-09-30 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StockMaster_app', '0006_alter_mensajes_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

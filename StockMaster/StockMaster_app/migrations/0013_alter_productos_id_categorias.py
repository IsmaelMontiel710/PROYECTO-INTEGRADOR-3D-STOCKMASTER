# Generated by Django 4.2.5 on 2023-10-02 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0012_productos_id_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id_categorias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StockMaster_app.categoria'),
        ),
    ]

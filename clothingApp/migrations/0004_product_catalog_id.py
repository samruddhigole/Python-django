# Generated by Django 3.2.24 on 2024-03-05 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothingApp', '0003_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catalog_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothingApp.catalog'),
        ),
    ]

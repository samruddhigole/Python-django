# Generated by Django 3.2.24 on 2024-02-26 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20240226_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='catalog_id',
        ),
    ]

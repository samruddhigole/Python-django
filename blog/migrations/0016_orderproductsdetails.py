# Generated by Django 3.2.24 on 2024-03-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProductsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.IntegerField(null=True)),
                ('product_quantity', models.IntegerField(null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('order_id', models.IntegerField(null=True)),
            ],
        ),
    ]

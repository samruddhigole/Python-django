# Generated by Django 3.2.24 on 2024-02-26 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20240226_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_id', models.IntegerField()),
                ('catalog_name', models.CharField(max_length=200)),
                ('catalog_Desc', models.CharField(max_length=200)),
                ('sort_order', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='productdetails',
            name='warrenty',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='catalog_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.catalog'),
        ),
    ]
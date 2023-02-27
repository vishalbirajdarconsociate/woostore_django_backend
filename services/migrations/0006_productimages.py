# Generated by Django 4.1 on 2023-02-21 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_delete_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/img/product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.product')),
            ],
        ),
    ]
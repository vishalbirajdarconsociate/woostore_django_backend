# Generated by Django 4.1 on 2023-02-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_customer_customerimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerImg',
            field=models.ImageField(blank=True, default='static/img/default/customer/default_user.png', upload_to='static/img/customer/'),
        ),
    ]
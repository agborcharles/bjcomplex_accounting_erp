# Generated by Django 4.0.3 on 2022-03-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0002_alter_bakerysales_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakerysales',
            name='customer',
            field=models.CharField(max_length=200, verbose_name='Customer'),
        ),
    ]
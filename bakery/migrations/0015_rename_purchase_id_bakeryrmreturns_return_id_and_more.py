# Generated by Django 4.0.3 on 2022-03-10 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0014_alter_bakeryinventory_stock_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bakeryrmreturns',
            old_name='purchase_id',
            new_name='return_id',
        ),
        migrations.RenameField(
            model_name='bakeryrmreturns',
            old_name='procuement_manager',
            new_name='return_manager',
        ),
    ]
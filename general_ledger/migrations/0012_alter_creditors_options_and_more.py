# Generated by Django 4.0.3 on 2022-03-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_ledger', '0011_alter_purchases_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditors',
            options={'verbose_name': 'Creditor', 'verbose_name_plural': 'Creditors'},
        ),
        migrations.RemoveField(
            model_name='creditors',
            name='stock_accnt_inv_id',
        ),
        migrations.AddField(
            model_name='creditors',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Payment Id'),
        ),
    ]

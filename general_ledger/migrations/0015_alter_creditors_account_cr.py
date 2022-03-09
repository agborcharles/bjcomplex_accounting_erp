# Generated by Django 4.0.3 on 2022-03-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_ledger', '0014_alter_creditors_account_dr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditors',
            name='account_cr',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash')], default='', max_length=500, null=True, verbose_name='Account Credit'),
        ),
    ]

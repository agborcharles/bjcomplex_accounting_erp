# Generated by Django 4.0.3 on 2022-03-04 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general_ledger', '0005_alter_income_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery'), ('Boulangerie', 'Boulangerie'), ('Supermarket', 'Supermarket'), ('Bar', 'Bar'), ('Snack', 'Snack'), ('Ice Cream', 'Ice Cream')], default='', max_length=500, null=True)),
                ('user_status', models.CharField(blank=True, choices=[('Employee', 'Employee'), ('Management', 'Management')], default='', max_length=500, null=True)),
                ('customer_institution', models.CharField(default='', max_length=200, verbose_name='Customer/Institution')),
                ('invoice_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Invoice Id')),
                ('stock_accnt_inv_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Stock Accnt Invoice Id')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.FloatField(default=0.0)),
                ('account_dr', models.CharField(blank=True, choices=[('Inventory', 'Inventory')], default='', max_length=500, null=True, verbose_name='Account Debit')),
                ('account_cr', models.CharField(blank=True, choices=[('Inventory', 'Inventory'), ('Inventory', 'Inventory')], default='', max_length=500, null=True, verbose_name='Account Credit')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
    ]

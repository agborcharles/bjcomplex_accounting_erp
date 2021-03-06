# Generated by Django 4.0.3 on 2022-03-04 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general_ledger', '0002_alter_openingbalance_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='openingbalance',
            name='customer_institution',
            field=models.CharField(default='', max_length=200, verbose_name='Customer/Supplier/Institution'),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(max_length=200)),
                ('user_status', models.CharField(blank=True, choices=[('Employee', 'Employee'), ('Management', 'Management')], default='', max_length=500, null=True)),
                ('customer_institution', models.CharField(default='', max_length=200, verbose_name='Customer/Institution')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.FloatField(default=0.0)),
                ('account_dr', models.CharField(max_length=200)),
                ('account_cr', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Income',
            },
        ),
    ]

# Generated by Django 2.2.12 on 2020-11-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('DA', 'Asset'), ('DE', 'Expense'), ('CL', 'Liability'), ('CE', 'Equity')], default='DA', max_length=2),
        ),
    ]

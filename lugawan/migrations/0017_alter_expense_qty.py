# Generated by Django 5.0.6 on 2024-05-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugawan', '0016_alter_expense_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='Qty',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

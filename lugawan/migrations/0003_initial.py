# Generated by Django 5.0.6 on 2024-05-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lugawan', '0002_delete_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
                ('branch_address', models.CharField(max_length=250)),
            ],
        ),
    ]

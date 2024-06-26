# Generated by Django 5.0.6 on 2024-05-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugawan', '0009_remove_halin_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=150)),
                ('transdate', models.DateTimeField(null=True)),
                ('expense', models.CharField(max_length=150)),
                ('price', models.FloatField(null=True)),
                ('notes', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='halin',
            name='transdate',
            field=models.DateTimeField(null=True),
        ),
    ]

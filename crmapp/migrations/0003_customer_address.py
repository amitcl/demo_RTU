# Generated by Django 5.0.4 on 2024-05-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_customer_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-13 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='Responsetype',
            new_name='emailaddress',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='Responsetext',
            new_name='responsetext',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='emailaddree',
            new_name='responsetype',
        ),
    ]

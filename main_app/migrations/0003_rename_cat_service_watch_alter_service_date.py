# Generated by Django 4.1.2 on 2022-10-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='cat',
            new_name='watch',
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(verbose_name='service date'),
        ),
    ]
# Generated by Django 5.1 on 2024-08-17 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0006_alter_attributemodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='key',
            options={'verbose_name': 'Key', 'verbose_name_plural': 'Keys'},
        ),
        migrations.AlterModelOptions(
            name='value',
            options={'verbose_name': 'Value', 'verbose_name_plural': 'Values'},
        ),
    ]

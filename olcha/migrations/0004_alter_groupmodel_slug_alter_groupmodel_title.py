# Generated by Django 5.0.7 on 2024-08-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0003_key_value_groupmodel_productmodel_imagemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='title',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-20 05:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0014_productcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='uploads/% Y/% m/% d/'), size=4),
        ),
    ]
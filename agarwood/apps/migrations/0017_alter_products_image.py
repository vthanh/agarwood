# Generated by Django 4.2.1 on 2023-05-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]

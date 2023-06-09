# Generated by Django 4.2.1 on 2023-05-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_alter_imageelement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageelement',
            name='name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='images',
        ),
        migrations.AddField(
            model_name='imageelement',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='apps.products'),
        ),
    ]

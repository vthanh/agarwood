# Generated by Django 2.2.5 on 2020-11-17 01:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_store_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

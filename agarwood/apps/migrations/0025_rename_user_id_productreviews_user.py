# Generated by Django 4.2.1 on 2023-05-20 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0024_rename_user_productreviews_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreviews',
            old_name='user_id',
            new_name='user',
        ),
    ]

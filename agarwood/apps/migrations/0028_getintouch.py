# Generated by Django 4.2.1 on 2023-05-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0027_alter_newscategory_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]

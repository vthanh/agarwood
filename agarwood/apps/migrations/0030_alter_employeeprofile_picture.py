# Generated by Django 4.2.1 on 2023-06-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0029_employeeposition_employeeprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='picture',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-11 03:29

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('number_of_store', models.IntegerField(blank=True, default=0)),
                ('tax', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('key_word', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=8)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('banner', models.FileField(upload_to='')),
                ('logo', models.FileField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('website', models.URLField()),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('zipcode', models.CharField(blank=True, max_length=200)),
                ('longitude', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('latitude', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('introduction', models.TextField(blank=True)),
                ('about_us', models.TextField(blank=True)),
                ('connection_num', models.IntegerField(blank=True, default=0)),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Company')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ot_monday', models.TimeField()),
                ('et_monday', models.TimeField()),
                ('ot_tuesday', models.TimeField()),
                ('et_tuesday', models.TimeField()),
                ('ot_wednesday', models.TimeField()),
                ('et_wednesday', models.TimeField()),
                ('ot_thursday', models.TimeField()),
                ('et_thursday', models.TimeField()),
                ('ot_friday', models.TimeField()),
                ('et_friday', models.TimeField()),
                ('ot_saturday', models.TimeField()),
                ('et_saturday', models.TimeField()),
                ('ot_sunday', models.TimeField()),
                ('et_sunday', models.TimeField()),
                ('timezone', models.CharField(max_length=100)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('store_type', models.ManyToManyField(related_name='store_type', to='apps.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.FileField(upload_to='')),
                ('price', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Store')),
            ],
        ),
        migrations.CreateModel(
            name='HistorySearching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=200)),
                ('key_word', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=8)),
                ('searching_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(blank=True, default=0.0)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(blank=True)),
                ('reviewing_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Store')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'store_id')},
            },
        ),
        migrations.CreateModel(
            name='OwnerStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Store')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_id', 'store_id')},
            },
        ),
    ]

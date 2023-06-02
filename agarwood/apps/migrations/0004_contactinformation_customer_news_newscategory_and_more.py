# Generated by Django 4.2.1 on 2023-05-17 08:53

import ckeditor.fields
import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0003_auto_20201117_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_created_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to='')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('key_word', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=8)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(blank=True, default=0.0)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(blank=True)),
                ('reviewing_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
                ('price', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('discount', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('total_number', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('sold_number', models.DecimalField(blank=True, decimal_places=20, max_digits=30)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='historysearching',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='media',
            name='store_id',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AlterUniqueTogether(
            name='ownerstore',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='ownerstore',
            name='store_id',
        ),
        migrations.RemoveField(
            model_name='ownerstore',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='store_id',
        ),
        migrations.AlterUniqueTogether(
            name='reviewstore',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='reviewstore',
            name='store_id',
        ),
        migrations.RemoveField(
            model_name='reviewstore',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='store',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='store',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='storetype',
            name='store_type',
        ),
        migrations.RemoveField(
            model_name='workingtime',
            name='store_id',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='HistorySearching',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='OwnerStore',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ReviewStore',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.DeleteModel(
            name='StoreType',
        ),
        migrations.DeleteModel(
            name='WorkingTime',
        ),
        migrations.AddField(
            model_name='productreviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apps.products'),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apps.products'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.newscategory'),
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_created_news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='productreviews',
            unique_together={('user_id', 'product')},
        ),
    ]

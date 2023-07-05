# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from datetime import datetime, timezone
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from meta.models import ModelMeta


User = get_user_model()


#
# class Company(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     email = models.EmailField()
#     phone = models.CharField(max_length=200, blank=True)
#     number_of_store = models.IntegerField(default=0, blank=True)
#     tax = models.CharField(max_length=100, blank=True)
#     created_at = models.DateTimeField(default=datetime.now)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Store(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     banner = models.FileField()
#     logo = models.FileField()
#     email = models.EmailField()
#     phone = models.CharField(max_length=20, blank=True)
#     website = models.URLField()
#     facebook = models.URLField()
#     instagram = models.URLField()
#     twitter = models.URLField()
#     zipcode = models.CharField(max_length=200, blank=True)
#     longitude = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
#     latitude = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
#     address = models.CharField(max_length=200, blank=True)
#     city = models.CharField(max_length=200, blank=True)
#     introduction = models.TextField(blank=True)
#     about_us = models.TextField(blank=True)
#     connection_num = models.IntegerField(default=0, blank=True)
#     company_id = models.ForeignKey(Company,  on_delete=models.CASCADE, blank=True, null=True)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  blank=True, null=True)
#     content = RichTextField(blank=False, null=False)
#
#     def __str__(self):
#         return self.name
#
#
# class OwnerStore(models.Model):
#     store_id = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
#
#     class Meta:
#         unique_together = (
#             'user_id',
#             'store_id',
#         )
#
#     def __str__(self):
#         return str(self.user_id) + ' - ' + str(self.store_id)
#
#
# class WorkingTime(models.Model):
#     ot_monday = models.TimeField()
#     et_monday = models.TimeField()
#     ot_tuesday = models.TimeField()
#     et_tuesday = models.TimeField()
#     ot_wednesday = models.TimeField()
#     et_wednesday = models.TimeField()
#     ot_thursday = models.TimeField()
#     et_thursday = models.TimeField()
#     ot_friday = models.TimeField()
#     et_friday = models.TimeField()
#     ot_saturday = models.TimeField()
#     et_saturday = models.TimeField()
#     ot_sunday = models.TimeField()
#     et_sunday = models.TimeField()
#     timezone = models.CharField(max_length=100)
#     store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
#
#
# class Media(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     url = models.URLField()
#     store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class StoreType(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     store_type = models.ManyToManyField(Store, related_name='store_type')
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     description = models.TextField(blank=True)
#     image = models.FileField()
#     price = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
#     created_at = models.DateTimeField(default=datetime.now)
#     store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Menu(models.Model):
#     name = models.CharField(max_length=200, blank=True)
#     key_word = ArrayField(models.CharField(max_length=100, blank=True), size=8,)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class HistorySearching(models.Model):
#     word = models.CharField(max_length=200, blank=True)
#     key_word = ArrayField(models.CharField(max_length=100, blank=True), size=8, )
#     searching_at = models.DateTimeField(default=datetime.now, blank=True)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#
#
# class ReviewStore(models.Model):
#     score = models.FloatField(default=0.0, blank=True)
#     title = models.CharField(max_length=200, blank=True)
#     content = models.TextField(blank=True)
#     reviewing_at = models.DateTimeField(default=datetime.now, blank=True)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = (
#             'user_id',
#             'store_id',
#         )
#

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, blank=True)
    key_word = ArrayField(models.CharField(max_length=255, blank=True), size=8, )
    description = models.TextField()
    image = models.ImageField(upload_to ='uploads/Y/m/d/', blank=True, null=True)
    is_parent_category =models.BooleanField(default=False) 
    parent_product_category = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def number_of_products(self):
        total = self.products_set.count()
        if self.is_parent_category:
            total = 0
            child_product_category_list = ProductCategory.objects.filter(parent_product_category=self)
            for child_product_category in child_product_category_list:
                total += child_product_category.products_set.count()
        return total


class Products(ModelMeta, models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = RichTextUploadingField(blank=False, null=False)
    cover_image = models.ImageField(upload_to ='uploads/Y/m/d/', blank=True, null=True)
    
    price = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
    discount = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
    total_number = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
    sold_number = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)

    _metadata = {
        'title': 'name',
        'description': 'description',
        'image': 'get_meta_image',
        'product_category': 'product_category'
    }

    def get_meta_image(self):
        if self.cover_image:
            return self.cover_image.url
        
    def __str__(self):
        return self.name
    
    @property
    def current_price(self):
        return round(self.price, 2)
    
    @property
    def real_price(self):
        return round(self.price - self.price * self.discount / 100, 2)
    

class ImageElement(models.Model):
    image = models.FileField(upload_to ='uploads/Y/m/d/')
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True, null=True)
    

class ProductImages(models.Model):
    image = models.ImageField(upload_to ='uploads/Y/m/d/')
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    

class ProductReviews(models.Model):
    score = models.FloatField(default=0.0, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    reviewing_at = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (
            'user_id',
            'product',
        )


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    unique_name = models.CharField(max_length=255)
    key_word = ArrayField(models.CharField(max_length=255, blank=True), size=8, )
    description = models.TextField()

    def __str__(self):
        return self.name


class News(ModelMeta, models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField()
    short_content = RichTextField(blank=False, null=False, default='')
    content = RichTextUploadingField(blank=False, null=False)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_created_news')

    _metadata = {
        'title': 'title',
        'short_content': 'short_content',
        'description': 'content',
        'image': 'get_meta_image',
    }

    def get_meta_image(self):
        if self.cover:
            return self.cover.url
        
    def __str__(self):
        return self.title


class Customer(models.Model):
    address = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_created_customer')


class ContactInformation(models.Model):
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class GetInTouch(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class EmployeePosition(models.Model):
    name = models.CharField(max_length=255)
    unique_name = models.CharField(max_length=255)
    key_word = ArrayField(models.CharField(max_length=255, blank=True), size=8, )
    description = models.TextField()

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField(upload_to ='uploads/')
    facebook = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True)
    whatsapp = models.CharField(max_length=255, null=True)
    tiktok = models.CharField(max_length=255, null=True)
    employee_position = models.ForeignKey(EmployeePosition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Voucher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField(upload_to ='uploads/')

    def __str__(self):
        return self.name



class AboutUs(ModelMeta, models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = RichTextUploadingField(blank=False, null=False)
    
    _metadata = {
        'title': 'name',
        'description': 'description',
    }
        
    def __str__(self):
        return self.title




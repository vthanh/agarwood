from django.contrib import admin
from django.conf import settings

from agarwood.apps.models import *

list_permission = settings.LIST_PERMISSION

from django.contrib.auth.models import Group
#
# list_permission = ['superAdmin', 'siteAdmin', 'assistantAdmin', 'storeAdmin', 'endUser']
#
admin.site.unregister(User)
admin.site.unregister(Group)
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'get_groups', 'email', 'first_name', 'last_name',)
#     list_filter = ('is_staff', 'is_superuser')
#     readonly_fields = ('password',)
#     filter_horizontal = ('groups',)
#
#     def get_queryset(self, request):
#         qs = super(UserAdmin, self).get_queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists():
#             return qs
#         if request.user.groups.filter(name=list_permission[1]).exists():
#             return qs.exclude(groups__name__in=list_permission[0:2])
#         return qs.filter(user_id=request.user)
#
#     def get_groups(self, obj):
#         return "\n".join([g.name for g in obj.groups.all()])
#
#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         if request.user.groups.filter(name=list_permission[1]).exists():
#             kwargs["queryset"] = Group.objects.exclude(name__in=list_permission[0:1])
#         if request.user.groups.filter(name=list_permission[2]).exists():
#             kwargs["queryset"] = Group.objects.exclude(name__in=list_permission[0:2])
#         return super().formfield_for_manytomany(db_field, request, **kwargs)
#
#
# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     filter_horizontal = ('permissions',)
#
#
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'tax', 'created_at')
#     search_fields = ['name', 'email']
#     readonly_fields = ['number_of_store']
#
#     def get_queryset(self, request):
#         qs = super(CompanyAdmin, self).get_queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists() \
#                 or request.user.groups.filter(name=list_permission[1]).exists() \
#                 or request.user.groups.filter(name=list_permission[2]).exists():
#             return qs
#         return qs.filter(user_id=request.user)
#
#
# @admin.register(Store)
# class StoreAdmin(admin.ModelAdmin):
#     list_display = ('name', 'banner', 'logo', 'email', 'phone', 'website', 'facebook', 'instagram', 'twitter', 'zipcode', 'longitude', 'latitude', 'address', 'content')
#     search_fields = ['name', 'banner', 'logo', 'email', 'phone', 'website', 'facebook', 'instagram', 'twitter', 'zipcode', 'longitude', 'latitude', 'address']
#     readonly_fields = ['user_id']
#
#     def save_model(self, request, instance, form, change):
#         user = request.user
#         instance = form.save(commit=False)
#         if not change or not instance.user_id:
#             instance.user_id = user
#         instance.user_id = user
#         instance.save()
#         form.save_m2m()
#         return instance
#
#     def get_queryset(self, request):
#         qs = super(StoreAdmin, self).get_queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists() \
#                 or request.user.groups.filter(name=list_permission[1]).exists()  \
#                 or request.user.groups.filter(name=list_permission[2]).exists():
#             return qs
#         return qs.filter(ownerstore__user_id=request.user)
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if not request.user.is_superuser and not request.user.groups.filter(name=list_permission[0]).exists() \
#                 and not request.user.groups.filter(name=list_permission[1]).exists() \
#                 and not request.user.groups.filter(name=list_permission[2]).exists():
#             return None
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
#
# @admin.register(OwnerStore)
# class OwnerStoreAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'store_id')
#
#
# @admin.register(WorkingTime)
# class WorkingTimeAdmin(admin.ModelAdmin):
#     list_display = ('store_id', 'ot_monday', 'et_monday', 'ot_tuesday', 'et_tuesday', 'ot_wednesday', 'et_wednesday', 'ot_thursday',
#                     'et_thursday', 'ot_friday', 'et_friday', 'ot_saturday', 'et_saturday', 'ot_sunday', 'et_sunday',
#                     'timezone')
#     search_fields = ['store_id', 'ot_monday', 'et_monday', 'ot_tuesday', 'et_tuesday', 'ot_wednesday', 'et_wednesday', 'ot_thursday',
#                      'et_thursday', 'ot_friday', 'et_friday', 'ot_saturday', 'et_saturday', 'ot_sunday', 'et_sunday',
#                      'timezone']
#
#     def get_queryset(self, request):
#         qs = super(WorkingTimeAdmin, self).get_queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists() \
#                 or request.user.groups.filter(name=list_permission[1]).exists() \
#                 or request.user.groups.filter(name=list_permission[2]).exists():
#             return qs
#         return qs.filter(store_id__in=Store.objects.filter(ownerstore__user_id=request.user))
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if not request.user.is_superuser and not request.user.groups.filter(name=list_permission[0]).exists() \
#                 and not request.user.groups.filter(name=list_permission[1]).exists() \
#                 and not request.user.groups.filter(name=list_permission[2]).exists():
#             kwargs["queryset"] = Store.objects.filter(ownerstore__user_id=request.user)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
#
# @admin.register(HistorySearching)
# class HistorySearchingAdmin(admin.ModelAdmin):
#     list_display = ('word', 'key_word', 'searching_at')
#     search_fields = ['word', 'key_word', 'searching_at']
#
#
# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'key_word')
#     search_fields = ['name', 'description', 'key_word']
#
#
# @admin.register(ReviewStore)
# class ReviewStoreAdmin(admin.ModelAdmin):
#     list_display = ('store_id', 'score', 'title', 'content', 'reviewing_at', 'user_id')
#     search_fields = ['store_id', 'score', 'title', 'content', 'reviewing_at', 'user_id']
#
#     def get_queryset(self, request):
#         qs = super(ReviewStoreAdmin, self).get_queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists() \
#                 or request.user.groups.filter(name=list_permission[1]).exists() \
#                 or request.user.groups.filter(name=list_permission[2]).exists():
#             return qs
#         return qs.filter(store_id__in=Store.objects.filter(ownerstore__user_id=request.user))
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'image', 'price', 'store_id', 'created_at')
#     search_fields = ['name', 'description', 'image', 'price', 'store_id', 'created_at']
#
#     def get_queryset(self, request):
#         qs = super(ProductAdmin, self).get_queryset(request)
#         if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists() \
#                 or request.user.groups.filter(name=list_permission[1]).exists() \
#                 or request.user.groups.filter(name=list_permission[2]).exists():
#             return qs
#         return qs.filter(store_id__in=Store.objects.filter(ownerstore__user_id=request.user))
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if not request.user.is_superuser and not request.user.groups.filter(name=list_permission[0]).exists() \
#                 and not request.user.groups.filter(name=list_permission[1]).exists() \
#                 and not request.user.groups.filter(name=list_permission[2]).exists():
#             kwargs["queryset"] = Store.objects.filter(ownerstore__user_id=request.user)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)


# @admin.register(Cleaner)
# class CleanerAdmin(admin.ModelAdmin):
#     list_display = (
#     'first_name', 'last_name', 'user_name', 'identify_number', 'identify_image', 'phone_number', 'skill', 'avatar')
#     search_fields = ['first_name', 'last_name', 'identify_number']
class ImageElementAdmin(admin.StackedInline):
    model = ImageElement


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ImageElementAdmin]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_category')
    search_fields = ['title']
    readonly_fields = ['user']

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.user = user
        instance.user = user
        instance.save()
        form.save_m2m()
        return instance


@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    pass


# # -*- coding: utf-8 -*-
# from __future__ import absolute_import, unicode_literals
#
# from django import forms
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from .models import User
#
#
# class MyUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User
#
#
# class MyUserCreationForm(UserCreationForm):
#
#     error_message = UserCreationForm.error_messages.update({
#         'duplicate_username': 'This username has already been taken.'
#     })
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     def clean_username(self):
#         username = self.cleaned_data["username"]
#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])
#
#
# @admin.register(User)
# class MyUserAdmin(AuthUserAdmin):
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')}
#          ),
#     )
#
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
#     search_fields = ['username', 'email', 'first_name', 'last_name']


from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# # Unregister the provided model admin
# admin.site.unregister(User)
#
#
# # Register out own model admin, based on the default UserAdmin
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     readonly_fields = [
#         'date_joined',
#     ]
#
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_superuser = request.user.is_superuser
#         disabled_fields = set()  # type: Set[str]
#
#         if not is_superuser:
#             disabled_fields |= {
#                 'username',
#                 'is_superuser',
#                 'user_permissions',
#             }
#
#         # Prevent non-superusers from editing their own permissions
#         if not is_superuser and obj is not None and obj == request.user:
#             disabled_fields |= {
#                 'is_staff',
#                 'is_superuser',
#                 'groups',
#                 'user_permissions',
#             }
#
#         for f in disabled_fields:
#             if f in form.base_fields:
#                 form.base_fields[f].disabled = True
#
#         return form

from django.contrib.auth.models import Group
from django.conf import settings

from .models import *


list_permission = settings.LIST_PERMISSION

admin.site.unregister(User)
admin.site.unregister(Group)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'get_groups', 'email', 'first_name', 'last_name',)
    list_filter = ('is_staff', 'is_superuser')
    readonly_fields = ('password',)
    filter_horizontal = ('groups',)

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name=list_permission[0]).exists():
            return qs
        if request.user.groups.filter(name=list_permission[1]).exists():
            return qs.exclude(groups__name__in=list_permission[0:2])
        return qs.filter(user_id=request.user)

    def get_groups(self, obj):
        return "\n".join([g.name for g in obj.groups.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if request.user.groups.filter(name=list_permission[1]).exists():
            kwargs["queryset"] = Group.objects.exclude(name__in=list_permission[0:2])
        if request.user.groups.filter(name=list_permission[2]).exists():
            kwargs["queryset"] = Group.objects.exclude(name__in=list_permission[0:3])
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('permissions',)

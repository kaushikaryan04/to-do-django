from django.contrib import admin
from .models import User , ToDo
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django import forms
from django.forms import TextInput, Textarea, CharField

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'name',)
    list_filter = ('email', 'username', 'name', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
admin.site.register(User , UserAdminConfig)
admin.site.register(ToDo)
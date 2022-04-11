from django.contrib import admin
from django.contrib.admin import register

from .models import User


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'middle_name')
    list_filter = ('is_staff', 'is_active', 'type')
    search_fields = ('email', 'phone_number')

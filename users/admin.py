from django.contrib import admin
from django.contrib.admin import register

from .models import User, Manager, Guest


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'middle_name')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'phone_number')
    exclude = ('password',)


@register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass


@register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.contrib.admin import register

from events.models import FirstTypeEvent, SecondTypeEvent, Application, Feedback
from users.models import User


class ApplicationAdminInline(admin.TabularInline):
    model = Application
    extra = 0

    def has_view_or_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.type == User.Type.MANAGER


class FeedbackAdminInline(admin.TabularInline):
    model = Feedback
    extra = 0


@register(FirstTypeEvent)
class FirstTypeEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'manager')
    readonly_fields = ('creation_date',)
    list_filter = ('manager__email',)
    inlines = (ApplicationAdminInline,)

    def has_view_permission(self, request, obj=None):
        if not request.user.is_anonymous:
            return request.user.is_superuser or request.user.type == User.Type.MANAGER
        else:
            return super(FirstTypeEventAdmin, self).has_module_permission(request)

    def has_module_permission(self, request):
        if not request.user.is_anonymous:
            return request.user.is_superuser or request.user.type == User.Type.MANAGER
        else:
            return super(FirstTypeEventAdmin, self).has_module_permission(request)


@register(SecondTypeEvent)
class SecondTypeEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'manager')
    readonly_fields = ('creation_date',)
    list_filter = ('manager__email',)
    inlines = (FeedbackAdminInline,)

    def has_view_permission(self, request, obj=None):
        if not request.user.is_anonymous:
            return request.user.is_superuser or request.user.type == User.Type.MANAGER
        else:
            return super(SecondTypeEventAdmin, self).has_module_permission(request)

    def has_module_permission(self, request):
        if not request.user.is_anonymous:
            return request.user.is_superuser or request.user.type == User.Type.MANAGER
        else:
            return super(SecondTypeEventAdmin, self).has_module_permission(request)

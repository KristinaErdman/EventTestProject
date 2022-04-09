from django.contrib import admin
from django.contrib.admin import register

from events.models import FirstTypeEvent, SecondTypeEvent, Application, Feedback


class ApplicationAdminInline(admin.TabularInline):
    model = Application
    extra = 0


class FeedbackAdminInline(admin.TabularInline):
    model = Feedback
    extra = 0


@register(FirstTypeEvent)
class FirstTypeEventAdmin(admin.ModelAdmin):
    inlines = (ApplicationAdminInline,)


@register(SecondTypeEvent)
class SecondTypeEventAdmin(admin.ModelAdmin):
    inlines = (FeedbackAdminInline,)

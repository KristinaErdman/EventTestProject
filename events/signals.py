from django.db.models import FileField

from .utils import delete_old_files


def post_delete_dispatcher_for_delete_old_files(sender, instance, **kwargs):
    for field in instance._meta.get_fields():
        if isinstance(field, FileField):
            attr = getattr(instance, field.name)
            delete_old_files(attr)


def pre_save_dispatcher_for_delete_old_files(sender, instance, **kwargs):
    if instance.pk:
        previous = instance.__class__.objects.get(pk=instance.pk)
        for field in instance._meta.get_fields():
            if isinstance(field, FileField):
                old_attr = getattr(previous, field.name)
                new_attr = getattr(instance, field.name)
                if old_attr != new_attr:
                    delete_old_files(old_attr)

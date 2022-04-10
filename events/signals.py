from django.core.mail import EmailMultiAlternatives
from django.db.models import FileField
from django.template.loader import get_template

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


def notify(sender, instance, **kwargs):
    subject = instance.__class__._meta.verbose_name
    if not instance.pk:
        try:
            template = get_template('emails/notify.html')
            body_letter = template.render({'instance': instance, })
            msg = EmailMultiAlternatives(to=(instance.event.manager.email,), subject=subject)
            msg.attach_alternative(body_letter, 'text/html')
            msg.send()
        except Exception as error:
            print(error)

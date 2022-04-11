from django.db import models
from django.db.models.signals import post_delete, pre_save

from users.models import User
from .signals import post_delete_dispatcher_for_delete_old_files, pre_save_dispatcher_for_delete_old_files, notify


class Event(models.Model):
    creation_date = models.DateField(auto_now_add=True, editable=False, verbose_name='Дата размещения')
    date = models.DateField(verbose_name='Дата проведения')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        abstract = True


class FirstTypeEvent(Event):
    manager = models.ForeignKey(User, limit_choices_to={'type': User.Type.MANAGER}, related_name='first_type_events',
                                on_delete=models.PROTECT,
                                verbose_name='Менеджер')

    class Meta:
        verbose_name = 'Событие первого типа'
        verbose_name_plural = 'События первого типа'


class SecondTypeEvent(Event):
    manager = models.ForeignKey(User, limit_choices_to={'type': User.Type.MANAGER}, related_name='second_type_events',
                                on_delete=models.PROTECT,
                                verbose_name='Менеджер')

    class Meta:
        verbose_name = 'Событие второго типа'
        verbose_name_plural = 'События второго типа'


class Application(models.Model):
    guest = models.ForeignKey(User, limit_choices_to={'type': User.Type.GUEST}, related_name='applications',
                              on_delete=models.CASCADE,
                              verbose_name='Гость')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    event = models.ForeignKey(FirstTypeEvent, related_name='applications', on_delete=models.CASCADE,
                              verbose_name='Событие')
    comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заявка на участие'
        verbose_name_plural = 'Заявки на участие'
        unique_together = (('event', 'guest'),)


class Feedback(models.Model):
    guest = models.ForeignKey(User, limit_choices_to={'type': User.Type.GUEST}, related_name='feedbacks',
                              on_delete=models.CASCADE, verbose_name='Гость')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    event = models.ForeignKey(SecondTypeEvent, related_name='feedbacks', on_delete=models.CASCADE,
                              verbose_name='Событие')
    file = models.FileField(null=True, blank=True, upload_to='feedbacks/', verbose_name='Файл')
    comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        unique_together = (('event', 'guest'),)


post_delete.connect(post_delete_dispatcher_for_delete_old_files, sender=Feedback)
pre_save.connect(pre_save_dispatcher_for_delete_old_files, sender=Feedback)

pre_save.connect(notify, sender=Application)
pre_save.connect(notify, sender=Feedback)

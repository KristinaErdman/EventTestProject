from django.db import models

from users.models import Manager, Guest


class Event(models.Model):
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата размещения')
    date = models.DateField(verbose_name='Дата проведения')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        abstract = True


class FirstTypeEvent(Event):
    manager = models.ForeignKey(Manager, related_name='first_type_events', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Событие первого типа'
        verbose_name_plural = 'События первого типа'


class SecondTypeEvent(Event):
    manager = models.ForeignKey(Manager, related_name='second_type_events', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Событие второго типа'
        verbose_name_plural = 'События второго типа'


class Application(models.Model):
    guest = models.ForeignKey(Guest, related_name='applications', on_delete=models.CASCADE, verbose_name='Гость')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    event = models.ForeignKey(FirstTypeEvent, related_name='applications', on_delete=models.CASCADE,
                              verbose_name='Событие')
    comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заявка на участие'
        verbose_name_plural = 'Заявки на участие'


class Feedback(models.Model):
    guest = models.ForeignKey(Guest, related_name='feedbacks', on_delete=models.CASCADE, verbose_name='Гость')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    event = models.ForeignKey(SecondTypeEvent, related_name='feedbacks', on_delete=models.CASCADE,
                              verbose_name='Событие')
    file = models.FileField(null=True, blank=True, upload_to='feedbacks/', verbose_name='Файл')
    comment = models.CharField(max_length=255, null=True, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
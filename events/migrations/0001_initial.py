# Generated by Django 4.0.3 on 2022-04-09 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondTypeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Дата размещения')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_type_events', to='users.manager')),
            ],
            options={
                'verbose_name': 'Событие второго типа',
                'verbose_name_plural': 'События второго типа',
            },
        ),
        migrations.CreateModel(
            name='FirstTypeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Дата размещения')),
                ('date', models.DateField(verbose_name='Дата проведения')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_type_events', to='users.manager')),
            ],
            options={
                'verbose_name': 'Событие первого типа',
                'verbose_name_plural': 'События первого типа',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('file', models.FileField(blank=True, null=True, upload_to='feedbacks/', verbose_name='Файл')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='events.secondtypeevent', verbose_name='Событие')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='users.guest', verbose_name='Гость')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='events.firsttypeevent', verbose_name='Событие')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='users.guest', verbose_name='Гость')),
            ],
            options={
                'verbose_name': 'Заявка на участие',
                'verbose_name_plural': 'Заявки на участие',
            },
        ),
    ]

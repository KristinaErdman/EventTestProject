# Generated by Django 4.0.3 on 2022-04-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_application_guest_alter_feedback_guest_and_more'),
        ('users', '0002_remove_guest_is_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('manager', 'Менеджер'), ('guest', 'Гость')], default='guest', max_length=7, verbose_name='Тип пользователя'),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]

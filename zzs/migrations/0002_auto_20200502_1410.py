# Generated by Django 3.0.5 on 2020-05-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mostvaluableplayer',
            name='full_name',
        ),
        migrations.AddField(
            model_name='mostvaluableplayer',
            name='first_name',
            field=models.CharField(default='NNN', max_length=100, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='mostvaluableplayer',
            name='last_name',
            field=models.CharField(default='NNN', max_length=100, verbose_name='Фамилия'),
        ),
    ]

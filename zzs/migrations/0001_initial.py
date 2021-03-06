# Generated by Django 3.0.5 on 2020-05-01 08:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата проведения')),
                ('prize_pool', models.IntegerField(default=0, help_text='указывать сумму в тенге', verbose_name='Призовой фонд')),
                ('lan', models.BooleanField(default=False, verbose_name='True- LAN, False- Online')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.CharField(max_length=300, verbose_name='Команды')),
                ('score', models.CharField(max_length=50, verbose_name='Счет')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='MostValuablePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=150, verbose_name='Ник')),
                ('full_name', models.CharField(max_length=150, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'MVP player',
                'verbose_name_plural': 'MVP players',
            },
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kd_ratio', models.FloatField(default=1.0, verbose_name='КД')),
                ('head_shots', models.FloatField(default=0.0, verbose_name='Процент хедшотов')),
                ('maps_played', models.IntegerField(default=0, verbose_name='Сыгранно карт')),
                ('elo', models.PositiveSmallIntegerField(default=1000, verbose_name='ОЧКОв ЭЛО')),
                ('face_it_lvl', models.PositiveSmallIntegerField(default=3, verbose_name='Уровень на FACEIT')),
            ],
            options={
                'verbose_name': 'Stat',
                'verbose_name_plural': 'Stats',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('team_started', models.DateField(default=datetime.date.today, verbose_name='Дата основания')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('matches', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.Match', verbose_name='Матчи')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(default=16, verbose_name='Возраст')),
                ('role', models.CharField(max_length=150, verbose_name='Роль')),
                ('photo', models.ImageField(upload_to='player/', verbose_name='Фото')),
                ('active_period', models.CharField(max_length=150, verbose_name='Период активности')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.Event', verbose_name='турниры')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zzs.MostValuablePlayer', verbose_name='игрок')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zzs.Stat', verbose_name='статистика')),
                ('team', models.ManyToManyField(related_name='team_player', to='zzs.Team', verbose_name='команда')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='mvp_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.MostValuablePlayer', verbose_name='MVP игрок'),
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Название')),
                ('preview', models.ImageField(upload_to='preview/', verbose_name='Превью')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.Match', verbose_name='матч')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.Player', verbose_name='игрок')),
            ],
            options={
                'verbose_name': 'Highlight',
                'verbose_name_plural': 'Highlights',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(verbose_name='Описание')),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zzs.Highlight', verbose_name='хайлайт')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.Comments', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]

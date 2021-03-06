# Generated by Django 3.1.2 on 2020-10-22 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50, verbose_name='Название Альбома')),
                ('number_of_songs', models.IntegerField(verbose_name='Кол-во песен в альбоме')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия автора')),
                ('group_name', models.CharField(max_length=50, verbose_name='Название группы')),
                ('group_role', models.CharField(max_length=50, verbose_name='Роль в группе')),
                ('author_info', models.TextField(verbose_name='Информация об авторе')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50, verbose_name='Название песни')),
                ('album_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_app.album')),
            ],
        ),
        migrations.CreateModel(
            name='Play_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_app.album')),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_app.author')),
                ('song_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_app.song')),
            ],
        ),
    ]

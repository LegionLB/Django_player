from django.db import models


class Author(models.Model):

    name = models.CharField("Имя автора", max_length=50)
    surname = models.CharField("Фамилия автора", max_length=50)
    group_name = models.CharField("Название группы", max_length=50)
    group_role = models.CharField("Роль в группе", max_length=50)
    author_info = models.TextField("Информация об авторе")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Album(models.Model):
    album_name = models.CharField("Название Альбома", max_length=50)
    number_of_songs = models.IntegerField("Кол-во песен в альбоме")

    def __str__(self):
        return self.album_name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

class Song(models.Model):
    album_name = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    song_name = models.CharField('Название песни', max_length=50)

    def __str__(self):
        return self.song_name

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

class Play_list(models.Model):
    author_name = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    album_name = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    song_name = models.ForeignKey(to=Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name

    class Meta:
        verbose_name = "Плей-лист"
        verbose_name_plural = "Плей-листы"

# Create your models here.

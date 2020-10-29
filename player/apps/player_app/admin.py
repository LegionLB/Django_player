from django.contrib import admin
from .models import Author, Song, Album, Play_list


# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'group_name')
    fields = ['name', 'surname', ('group_name', 'group_role'), 'author_info']
    list_filter = ('name', 'group_name')


admin.site.register(Author, AuthorAdmin)


# admin.site.register(Song)
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'album_name')


# admin.site.register(Album)
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'album_author_name')
    list_filter = ['album_author_name']


# admin.site.register(Play_list)
@admin.register(Play_list)
class Play_listAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'album_name', 'author_name')
    list_filter = ('album_name', 'song_name')

# Register your models here.

from django.contrib import admin
from .models import Author, Song, Album, Play_list

admin.site.register(Author)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Play_list)


# Register your models here.

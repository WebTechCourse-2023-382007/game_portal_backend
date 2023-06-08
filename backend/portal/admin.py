from django.contrib import admin
from .models import Tag
from .models import Game
from .models import GameTag


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'releaseYear', 'publisher', 'logoUrl')


class GameTagAdmin(admin.ModelAdmin):
    list_display = ('game', 'tag')


# Register your models here.

admin.site.register(Tag, TagAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameTag, GameTagAdmin)

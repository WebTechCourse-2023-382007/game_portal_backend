from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')

# Register your models here.

admin.site.register(Tag, TagAdmin)
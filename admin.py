from django.contrib import admin

from . import models

class DictionaryAdmin(admin.ModelAdmin):
    list_filter = [
        'type', 'active'
    ]

admin.site.register(models.Dictionary, DictionaryAdmin)
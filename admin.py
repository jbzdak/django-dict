__author__ = 'jb'


from django.contrib import admin

import models

import forms

class DictionaryAdmin(admin.ModelAdmin):
    list_filter = [
        'type', 'active'
    ]
    readonly_fields = [
        'user_changed'
    ]

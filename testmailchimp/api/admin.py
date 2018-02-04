from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
    list_filter = ('name', 'body')
    search_fields = ('name', 'body')

admin.site.register(models.ContactForm)

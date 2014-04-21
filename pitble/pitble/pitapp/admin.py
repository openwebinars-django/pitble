from django.contrib import admin

from pitble.pitapp.models import Pitble


class PitbleAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner')
    search_fields = ('text',)

admin.site.register(Pitble, PitbleAdmin)
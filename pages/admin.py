from django.contrib import admin
from django.utils.html import format_html

from pages.models import Slider, Contacts

site_header = 'Ply-Art Админ панель'


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_display_links = ('title', 'is_active', 'created_at')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address')
    list_display_links = ('phone_number', 'email', 'address')


admin.site.register(Slider, SliderAdmin)
admin.site.register(Contacts, ContactsAdmin)

# register admin name
admin.site.site_header = format_html(site_header)


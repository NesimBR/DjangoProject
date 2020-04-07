from django.contrib import admin

# Register your models here.
from home.models import Setting, Contactform


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


admin.site.register(Contactform, ContactFormAdmin)
admin.site.register(Setting, SettingAdmin)

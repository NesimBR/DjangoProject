from django.contrib import admin

# Register your models here.
from home.models import Setting, Contactform, UserProfile


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'university', 'department', 'image_tag']

admin.site.register(Contactform, ContactFormAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(UserProfile,UserProfileAdmin)


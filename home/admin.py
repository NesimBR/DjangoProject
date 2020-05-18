from django.contrib import admin

# Register your models here.
from home.models import Setting, Contactform, UserProfile, FAQ


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'university', 'department', 'image_tag']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'create_at' ]
    list_filter = ['status']


admin.site.register(Contactform, ContactFormAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FAQ, FAQAdmin)


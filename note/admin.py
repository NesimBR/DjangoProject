from django.contrib import admin

# Register your models here.
from note.models import Note, Category, Images


class NoteImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'Category', 'image_tag', 'create_at', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'Category']
    inlines = [NoteImageInline]



class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'note', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Images, ImagesAdmin)

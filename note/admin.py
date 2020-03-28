from django.contrib import admin

# Register your models here.
from note.models import Note, Category, Images


class NoteImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'Category', 'create_at', 'status']
    list_filter = ['status', 'Category']
    inlines = [NoteImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'note', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Images, ImagesAdmin)

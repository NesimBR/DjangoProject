from django.contrib import admin

# Register your models here.
from note.models import Note, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'Category', 'create_at', 'status']
    list_filter = ['status', 'Category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)

from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from note.models import Note, Category, Images, Comment


class NoteImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'Category','user', 'image_tag', 'create_at', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'Category']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [NoteImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'note', 'image_tag']
    readonly_fields = ('image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Note,
                'Category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Note,
                 'Category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'note', 'user', 'status']
    list_filter = ['status']


admin.site.register(Category,  CategoryAdmin2)
admin.site.register(Note, NoteAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)

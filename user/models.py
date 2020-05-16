from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.forms import ModelForm, forms, TextInput, Select, FileInput

from note.models import Note, Category


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['Category', 'title', 'slug', 'description', 'keywords', 'image', 'detail']
        widgets = {
            'Category': Select(attrs={'class': 'input','placeholder': 'Category'}, choices=Category.objects.all()),

            'title': TextInput(attrs={'class': 'input form-control', 'placeholder': 'title'}),
            'slug': TextInput(attrs={'class': 'input form-control', 'placeholder': 'slug'}),
            'description': TextInput(attrs={'class': 'input form-control', 'placeholder': 'description'}),
            'keywords': TextInput(attrs={'class': 'input form-control', 'placeholder': 'keywords'}),
            'image': FileInput(attrs={'class': 'input form-control'}),
            'detail': CKEditorWidget(),

        }
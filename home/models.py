from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
from django.forms import TextInput, ModelForm, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('True', 'true'),
        ('False', 'false')
    )
    title = models.CharField(max_length=150)
    description = models.CharField(blank=True,max_length=255)
    keywords = models.CharField(blank=True,max_length=255)
    company = models.CharField(blank=True,max_length=255)
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=100)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=10)
    icon = models.ImageField(blank=True, upload_to='image/')
    facebook = models.CharField(blank=True,max_length=150)
    twitter = models.CharField(blank=True,max_length=150)
    instagram = models.CharField(blank=True,max_length=150)
    aboutus = RichTextUploadingField(blank=True)
    contactus = RichTextUploadingField(blank=True)
    references =RichTextUploadingField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.icon.url))

    image_tag.short_description = 'Image'

class Contactform(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed')
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=250)
    note= models.CharField(blank=True, max_length=50)
    ip=models.CharField(blank=True, max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactFormu( ModelForm ):
    class Meta :
        model = Contactform
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control  span3 form-group', 'id': 'name', 'placeholder': 'Your Name'}),
            'email': TextInput(attrs={'class': 'form-control  span3 form-group', 'id': 'email', 'placeholder': 'Your Email'}),
            'subject': TextInput(attrs={'class': 'form-control span3 form-group', 'id': 'subject', 'placeholder':'Subject'}),
            'message': Textarea(attrs={'class': 'form-control  span3 margintop10 form-grou', 'style' : 'float:left; position: relative;','placeholder': 'Subject', 'rows': '2'}),
        }
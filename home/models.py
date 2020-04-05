from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
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

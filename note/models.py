from django.db import models


# Create your models here.
class Category(models.Model):
    # iki amaç var burada tablo oluşturması ve adminde ayarlamak
    STATUS = (
        ('True', 'true'),
        ('False', 'false')
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices= STATUS)
    image = models.ImageField(blank=True, upload_to='image/')
    slug = models.SlugField()  # id ile çağırmamak için metinsel olark çağırmak işlemi yapıyor
    # category iç içe çalışma mantığı var
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)  # cascad silme işleminde ona bağlı şeylerde silinir
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #  bundan sonra migrate yapmamızz lazım python manage.py makemigrations note ondan sonra migrate
    def __str__(self):
        return self.title
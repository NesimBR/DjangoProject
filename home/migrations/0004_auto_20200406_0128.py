# Generated by Django 3.0.4 on 2020-04-05 22:28

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200329_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contactus',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-27 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('True', 'true'), ('False', 'false')], max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='note.Category')),
            ],
        ),
    ]

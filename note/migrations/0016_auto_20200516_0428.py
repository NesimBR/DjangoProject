# Generated by Django 3.0.6 on 2020-05-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0015_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'true'), ('False', 'false')], default='New', max_length=10),
        ),
    ]
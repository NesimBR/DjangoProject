# Generated by Django 3.0.4 on 2020-04-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200407_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='note',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

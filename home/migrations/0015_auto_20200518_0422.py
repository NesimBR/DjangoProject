# Generated by Django 3.0.6 on 2020-05-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_faq_ordernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='ordernumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

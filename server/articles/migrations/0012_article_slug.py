# Generated by Django 3.1.5 on 2021-01-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20210117_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='r'),
            preserve_default=False,
        ),
    ]

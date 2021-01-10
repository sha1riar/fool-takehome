# Generated by Django 3.1.5 on 2021-01-10 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='disclosure',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='publishDate',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='relatedInstruments',
            field=models.JSONField(default='[{}]'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.JSONField(default='[{}]'),
            preserve_default=False,
        ),
    ]

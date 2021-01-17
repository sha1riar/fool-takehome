# Generated by Django 3.1.5 on 2021-01-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='instrument',
            name='companyName',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrument',
            name='exchange',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrument',
            name='instrumentId',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrument',
            name='symbol',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='tagName',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='tagSlug',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='tagTypeName',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='tagTypeSlug',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
    ]

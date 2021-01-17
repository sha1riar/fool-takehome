# Generated by Django 3.1.5 on 2021-01-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='change',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='changePercent',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

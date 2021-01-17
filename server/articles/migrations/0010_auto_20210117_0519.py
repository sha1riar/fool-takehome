# Generated by Django 3.1.5 on 2021-01-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_tag_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='currentPrice',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instrument',
            name='openPrice',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]

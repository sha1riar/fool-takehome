# Generated by Django 3.1.5 on 2021-01-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210117_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='currentPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='openPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

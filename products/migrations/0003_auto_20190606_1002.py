# Generated by Django 2.2.2 on 2019-06-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190606_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_retail',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_wholesale',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]

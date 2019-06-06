# Generated by Django 2.2.2 on 2019-06-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('price_retail', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('price_wholesale', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('date', models.DateField()),
            ],
        ),
    ]

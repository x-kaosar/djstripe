# Generated by Django 3.2.13 on 2022-07-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default='10'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hots',
            field=models.BooleanField(default=False, verbose_name='Новинки'),
        ),
    ]

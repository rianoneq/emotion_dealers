# Generated by Django 4.2.4 on 2023-08-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_image_postproductimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
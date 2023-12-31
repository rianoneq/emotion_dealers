# Generated by Django 4.2.4 on 2023-08-14 19:08

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to=catalog.models.Product.upload_to),
        ),
        migrations.CreateModel(
            name='PostProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to=catalog.models.PostProductImage.upload_to)),
                ('prod', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]

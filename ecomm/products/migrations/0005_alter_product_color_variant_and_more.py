# Generated by Django 5.0.3 on 2024-03-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_colorvariant_sizevariant_product_color_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Color_Variant',
            field=models.ManyToManyField(blank=True, to='products.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='products.sizevariant'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-17 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_uuid_category_uid_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PrdouctImage',
            new_name='ProductImage',
        ),
    ]

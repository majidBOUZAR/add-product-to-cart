# Generated by Django 3.2.9 on 2021-12-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_products_snall_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='snall_description',
            new_name='small_description',
        ),
    ]

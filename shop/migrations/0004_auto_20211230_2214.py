# Generated by Django 2.2 on 2021-12-31 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-16 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
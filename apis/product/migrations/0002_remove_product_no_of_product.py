# Generated by Django 2.2.2 on 2019-08-26 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='no_of_product',
        ),
    ]
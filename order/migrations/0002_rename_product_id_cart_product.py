# Generated by Django 4.0.3 on 2022-04-20 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='product',
        ),
    ]
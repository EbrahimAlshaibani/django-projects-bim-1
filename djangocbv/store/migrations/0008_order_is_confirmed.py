# Generated by Django 4.2.6 on 2023-10-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_order_product_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(null=True, verbose_name='is confirmed'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_order_product_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='store.OrderItem', to='store.product'),
        ),
    ]
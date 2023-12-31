# Generated by Django 4.2.6 on 2023-10-23 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_setting_alter_category_name_alter_customer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_settings', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]

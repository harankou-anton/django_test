# Generated by Django 4.1.7 on 2023-04-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="external_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

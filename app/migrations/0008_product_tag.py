# Generated by Django 4.1.4 on 2023-01-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customer_order_product_tag_remove_model_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='app.tag'),
        ),
    ]

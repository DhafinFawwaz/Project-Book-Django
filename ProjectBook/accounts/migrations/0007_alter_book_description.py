# Generated by Django 4.1.2 on 2022-10-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_book_price_customer_balance_supplier_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]

# Generated by Django 4.0.5 on 2022-10-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_product_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.CharField(default='Not specified.', max_length=30),
        ),
    ]

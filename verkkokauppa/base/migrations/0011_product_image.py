# Generated by Django 4.0.5 on 2022-10-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_product_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_no_image.png', upload_to='product_images'),
        ),
    ]
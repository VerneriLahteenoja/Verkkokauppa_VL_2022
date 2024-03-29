# Generated by Django 4.0.5 on 2022-10-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default='-', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='-', max_length=30),
            preserve_default=False,
        ),
    ]

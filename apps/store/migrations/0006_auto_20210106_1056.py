# Generated by Django 3.1.4 on 2021-01-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210102_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/'),
        ),
    ]

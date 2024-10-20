# Generated by Django 5.1.1 on 2024-10-19 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0010_rename_categoria_blogpost_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Noticias.categoria'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=130, unique=True),
        ),
    ]
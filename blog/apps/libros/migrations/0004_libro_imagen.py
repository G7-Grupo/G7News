# Generated by Django 3.2.25 on 2024-09-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_libro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='libros'),
        ),
    ]

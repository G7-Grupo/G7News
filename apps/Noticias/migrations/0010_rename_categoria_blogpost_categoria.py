# Generated by Django 5.1.1 on 2024-10-18 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0009_alter_blogpost_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='Categoria',
            new_name='categoria',
        ),
    ]

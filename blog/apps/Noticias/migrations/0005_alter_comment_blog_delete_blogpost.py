# Generated by Django 5.1.1 on 2024-10-15 02:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0004_remove_blogpost_author_delete_profile'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.blogpost'),
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]

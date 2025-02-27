# Generated by Django 5.1.1 on 2024-09-28 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('imagen', models.ImageField(null=True, upload_to='libros')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Noticias.autor')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-15 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0006_blogpost_alter_comment_blog'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
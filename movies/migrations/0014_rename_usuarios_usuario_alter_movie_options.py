# Generated by Django 4.2.4 on 2023-09-22 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_usuarios_alter_movie_options_alter_movie_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuarios',
            new_name='Usuario',
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
    ]

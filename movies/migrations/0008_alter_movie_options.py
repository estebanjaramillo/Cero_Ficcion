# Generated by Django 4.2.4 on 2023-09-21 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_customuser_options_alter_movie_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'permissions': [('can_add_movie', 'Can add movie'), ('can_change_movie', 'Can change movie'), ('can_delete_movie', 'Can delete movie')]},
        ),
    ]

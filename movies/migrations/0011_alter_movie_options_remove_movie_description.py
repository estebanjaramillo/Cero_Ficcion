# Generated by Django 4.2.4 on 2023-09-22 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_alter_movie_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'permissions': [('can_add_movie', 'Can add movie')]},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
    ]

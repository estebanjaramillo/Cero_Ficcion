# Generated by Django 4.2.4 on 2023-10-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0034_alter_asistencia_options_alter_aula_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asd', models.DateField()),
                ('dasdirector', models.CharField(max_length=255)),
                ('asdas', models.TextField()),
            ],
            options={
                'permissions': [('can_add_pelicula', 'Can add pelicula')],
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'permissions': [('can_add_movie', 'Can add movie')]},
        ),
    ]
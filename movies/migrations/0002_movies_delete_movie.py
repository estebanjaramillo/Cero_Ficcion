# Generated by Django 4.2.4 on 2023-09-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]

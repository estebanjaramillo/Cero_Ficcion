# Generated by Django 4.2.4 on 2023-10-04 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0032_alter_estudiante_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='user',
        ),
    ]
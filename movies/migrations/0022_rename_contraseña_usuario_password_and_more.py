# Generated by Django 4.2.4 on 2023-09-27 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_rename_password_usuario_contraseña_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre_usuario',
            new_name='username',
        ),
    ]

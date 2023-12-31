# Generated by Django 4.2.4 on 2023-09-28 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_rename_contraseña_usuario_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula', models.CharField(max_length=150)),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('fecha_creacion', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.usuario')),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-04 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0029_rename_taller_calificacion_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.OneToOneField( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-27 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_usuario_customuser_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

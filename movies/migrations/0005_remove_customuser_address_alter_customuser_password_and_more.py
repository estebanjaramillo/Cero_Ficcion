# Generated by Django 4.2.4 on 2023-09-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]

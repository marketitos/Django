# Generated by Django 4.1.7 on 2023-03-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]

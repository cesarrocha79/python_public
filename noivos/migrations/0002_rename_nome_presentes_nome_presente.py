# Generated by Django 5.1.3 on 2024-11-06 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presentes',
            old_name='nome',
            new_name='nome_presente',
        ),
    ]

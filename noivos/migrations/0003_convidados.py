# Generated by Django 5.1.3 on 2024-11-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0002_rename_nome_presentes_nome_presente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convidados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_convidado', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(blank=True, max_length=25, null=True)),
                ('maximo_acompanhantes', models.PositiveIntegerField(default=0)),
                ('token', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('AC', 'Aguardando confirmação'), ('C', 'Confirmado'), ('R', 'Recusado')], default='AC', max_length=2)),
            ],
        ),
    ]

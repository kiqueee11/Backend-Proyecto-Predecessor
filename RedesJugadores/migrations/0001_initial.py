# Generated by Django 5.2 on 2025-04-23 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Jugadores', '0001_initial'),
        ('Redes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedesJugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=300, null=True, verbose_name='Link de la red social')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='red_social', to='Jugadores.jugador')),
                ('red', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='red_social', to='Redes.redsocial')),
            ],
            options={
                'verbose_name': 'Red_jugador',
                'verbose_name_plural': 'Redes_jugador',
                'db_table': 'redes_jugador',
            },
        ),
    ]

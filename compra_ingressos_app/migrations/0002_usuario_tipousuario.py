# Generated by Django 5.1.4 on 2024-12-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra_ingressos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.IntegerField(default=0),
        ),
    ]

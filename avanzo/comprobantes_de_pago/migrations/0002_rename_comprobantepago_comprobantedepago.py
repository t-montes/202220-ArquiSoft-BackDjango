# Generated by Django 3.2.6 on 2022-09-30 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
        ('comprobantes_de_pago', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ComprobantePago',
            new_name='ComprobanteDePago',
        ),
    ]

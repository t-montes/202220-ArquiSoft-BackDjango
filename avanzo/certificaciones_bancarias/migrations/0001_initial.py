# Generated by Django 3.2.6 on 2022-09-30 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificacionBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cuenta', models.BigIntegerField()),
                ('tipo_cuenta', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_vencimiento', models.DateField()),
                ('gerente_banco', models.CharField(max_length=50)),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
            ],
        ),
    ]

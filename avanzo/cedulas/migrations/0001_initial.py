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
            name='Cedula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=50)),
                ('lugar_expedicion', models.CharField(max_length=50)),
                ('fecha_expedicion', models.DateField()),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
            ],
        ),
    ]

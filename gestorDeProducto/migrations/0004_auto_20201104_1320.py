# Generated by Django 3.1.2 on 2020-11-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProducto', '0003_auto_20201102_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('direccion', models.TextField(max_length=100)),
                ('telefono', models.TextField(max_length=100)),
                ('encargado', models.TextField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='Nombre',
            new_name='nombre',
        ),
    ]

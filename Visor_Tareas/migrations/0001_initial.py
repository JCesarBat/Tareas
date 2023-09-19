# Generated by Django 4.1.7 on 2023-08-21 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipado_de_Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='Visor')),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_Final', models.DateField()),
                ('hora', models.TimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visor_Tareas.tipado_de_tareas')),
            ],
        ),
    ]

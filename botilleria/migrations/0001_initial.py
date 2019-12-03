# Generated by Django 2.2.6 on 2019-12-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
    ]
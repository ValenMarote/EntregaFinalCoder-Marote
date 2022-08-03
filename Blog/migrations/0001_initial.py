# Generated by Django 4.0.6 on 2022-07-20 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=120, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen_referencial', models.ImageField(blank=True, null=True, upload_to='autores/', verbose_name='Imagen Referencial')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/Categoria Desactivada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, unique=True, verbose_name='Título del Post')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('contenido', models.TextField()),
                ('imagen_referencial', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen Referencial')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado / No Publicado')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de Publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
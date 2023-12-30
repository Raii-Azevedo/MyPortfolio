# Generated by Django 4.1.10 on 2023-12-30 03:10

import ckeditor.fields
import ckeditor_uploader.fields
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('about', models.CharField(blank=True, max_length=200, verbose_name='Cargo')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('college', models.CharField(max_length=200, verbose_name='College')),
                ('year', models.CharField(max_length=30, verbose_name='Year')),
                ('class_description', models.TextField(max_length=500, verbose_name='Job')),
                ('company', models.CharField(max_length=200, verbose_name='Company')),
                ('job_year', models.CharField(max_length=30, verbose_name='Year')),
                ('job_description', models.TextField(max_length=500, verbose_name='Job')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('short', models.CharField(max_length=300, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Homes',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('project', models.CharField(max_length=200, verbose_name='Project Name')),
                ('project_desc', models.TextField(max_length=300, verbose_name='Project')),
                ('proj_img', imagekit.models.fields.ProcessedImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('icone', models.CharField(choices=[('bx-code-alt', 'Web'), ('bx-line-chart', 'Análise'), ('bxs-dashboard', 'Dashboard')], max_length=15, verbose_name='Icone')),
                ('service', models.CharField(max_length=200, verbose_name='Service')),
                ('service_desc', models.TextField(max_length=300, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('resume', ckeditor.fields.RichTextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='YouTube URL')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

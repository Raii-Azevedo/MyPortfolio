# Generated by Django 4.0.2 on 2024-02-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_services_icone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Projeto'},
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='modificado',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_images/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.CharField(max_length=400, verbose_name='Descrição'),
        ),
    ]
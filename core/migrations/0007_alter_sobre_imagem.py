# Generated by Django 4.2 on 2023-04-29 21:23

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobre',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='about', variations={'thumb': {'crop': True, 'height': 550, 'width': 508}}, verbose_name='Imagem'),
        ),
    ]

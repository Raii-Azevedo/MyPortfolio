# Generated by Django 4.0.2 on 2024-02-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_experience_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icone',
            field=models.CharField(choices=[('bx bxs-dashboard', 'dashboard'), ('bx bx-line-chart', 'gráfico'), ('bx bx-code-alt', 'developer')], default='bx-code-alt', max_length=20, verbose_name='Icone'),
        ),
    ]
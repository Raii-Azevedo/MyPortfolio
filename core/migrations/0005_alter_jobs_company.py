# Generated by Django 4.0.2 on 2024-02-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_jobs_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='company',
            field=models.CharField(default='Freelance', max_length=300, verbose_name='Company'),
        ),
    ]
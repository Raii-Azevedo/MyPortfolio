# Generated by Django 4.0.2 on 2024-02-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_jobs_alter_experience_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company',
            field=models.CharField(default='Freelance', max_length=300, verbose_name='Cargo'),
        ),
    ]

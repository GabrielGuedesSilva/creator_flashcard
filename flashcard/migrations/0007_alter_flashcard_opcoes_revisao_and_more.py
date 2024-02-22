# Generated by Django 5.0.2 on 2024-02-21 13:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0006_alter_flashcard_frase_aplicacao_verso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='opcoes_revisao',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=list, null=True, size=4),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='traducao_verso',
            field=models.CharField(default='', max_length=255),
        ),
    ]

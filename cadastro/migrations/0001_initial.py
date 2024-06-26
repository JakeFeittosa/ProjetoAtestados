# Generated by Django 5.0.4 on 2024-05-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InserirFalta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=100)),
                ('ano_aluno', models.IntegerField(max_length=1)),
                ('turma_aluno', models.CharField(max_length=3)),
                ('data_afastamente', models.DateField()),
                ('dias_afastado', models.IntegerField(max_length=3)),
                ('justificativa', models.TextField()),
                ('arquivo', models.CharField(max_length=100)),
            ],
        ),
    ]

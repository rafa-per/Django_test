# Generated by Django 5.0.6 on 2024-05-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('curso', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=20)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('telefone1', models.CharField(max_length=14)),
                ('telefone2', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Defeito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDePagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('loggin', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('valor', models.FloatField()),
                ('comentarios', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efetuado', models.BooleanField()),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('valor', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=25)),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('saida', models.DateTimeField()),
                ('finalizado', models.BooleanField()),
                ('comentarios', models.TextField()),
            ],
        ),
    ]

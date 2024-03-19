# Generated by Django 5.0.3 on 2024-03-19 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_management', '0003_alter_research_options_research_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheduledtimes',
            options={'verbose_name': 'Pesquisa com horário marcado', 'verbose_name_plural': 'Pesquisas com horários marcados'},
        ),
        migrations.RemoveField(
            model_name='research',
            name='assigned_room',
        ),
        migrations.AlterField(
            model_name='research',
            name='conep_approvement_date',
            field=models.DateField(default=datetime.date.today, help_text='Data de aprovação do CONEP (Comitê de Ética em Pesquisa).', verbose_name='Data de Aprovação do CONEP'),
        ),
        migrations.AlterField(
            model_name='research',
            name='ending_date',
            field=models.DateField(default=datetime.date.today, help_text='Data de término prevista.', verbose_name='Data de Término'),
        ),
        migrations.AlterField(
            model_name='research',
            name='expected_number_of_patients',
            field=models.IntegerField(default=1, help_text='Número previsto de pacientes/voluntários no estudo.', verbose_name='Número de Pacientes'),
        ),
        migrations.AlterField(
            model_name='research',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Desmarcar quando um projeto não apresentar atividade após 120 dias.', verbose_name='Ativa'),
        ),
        migrations.AlterField(
            model_name='research',
            name='start_date',
            field=models.DateField(default=datetime.date.today, help_text='Data de início prevista.', verbose_name='Data de Início'),
        ),
    ]
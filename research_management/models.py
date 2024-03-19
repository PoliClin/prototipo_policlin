from datetime import date

from django.conf import settings
from django.db import models
from rooms.models import Room
from system_constants.models import Schedule, Weekdays


class Research(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome da pesquisa")
    main_researcher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name= 'main_researcher', on_delete=models.SET_NULL, null =True, verbose_name="Pesquisador Principal")
    researchers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name= 'researchers', verbose_name="Pesquisadores")
    conep_approvement_date = models.DateField(default= date.today, null = False, help_text="Data de aprovação do CONEP (Comitê de Ética em Pesquisa).", verbose_name="Data de Aprovação do CONEP")
    start_date = models.DateField(default= date.today, null = False, help_text="Data de início prevista.", verbose_name="Data de Início")
    ending_date = models.DateField(default= date.today, null = False, help_text="Data de término prevista.", verbose_name="Data de Término")
    expected_number_of_patients =  models.IntegerField(default= 1, verbose_name="Número de Pacientes", null=False, blank=False, help_text="Número previsto de pacientes/voluntários no estudo.")
    outpatient_care = models.BooleanField(verbose_name="Atendimento ambulatorial", default=False, null = False, blank= False)
    is_active = models.BooleanField(verbose_name = "Ativa", default=True, null=False, blank=False, help_text="Desmarcar quando um projeto não apresentar atividade após 120 dias.")
    #assigned_room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Sala atribuída", help_text="Sala atribuída ao projeto, caso ainda não possua, deixar em branco.")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Pesquisa cadastrada"
        verbose_name_plural = "Pesquisas cadastradas"



class ScheduledTimes(models.Model):
    start_schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE ,related_name='start_schedule', verbose_name="Horário de Início", )
    end_schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE ,related_name='end_schedule', verbose_name="Horário de Término", )
    weekday = models.ManyToManyField(Weekdays, verbose_name="Dias da semana", blank=True)
    research = models.ForeignKey(Research, on_delete=models.CASCADE, verbose_name="Pesquisa")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Sala")

    def __str__(self):
        return f"{self.research} - {self.room}"
    
    class Meta:
        verbose_name = "Pesquisas com horário marcado"
        verbose_name_plural = "Pesquisas com horários marcados"

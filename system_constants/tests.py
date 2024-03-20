from django.test import TestCase
from .models import Weekdays, Schedule
from .apps import SystemConstantsConfig
from datetime import time


class WeekdaysModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando um objeto Weekdays para uso nos testes
        Weekdays.objects.create(name='Segunda-feira')

    def test_str_method(self):
        """
        O método __str__() de Weekdays deve retornar o nome do dia da semana.
        """
        weekday = Weekdays.objects.get(name='Segunda-feira')
        self.assertEqual(str(weekday), 'Segunda-feira')

    def test_verbose_name(self):
        """
        O verbose_name da classe Meta em Weekdays deve ser 'Dia da semana'.
        """
        self.assertEqual(Weekdays._meta.verbose_name, 'Dia da semana')

    def test_verbose_name_plural(self):
        """
        O verbose_name_plural da classe Meta em Weekdays deve ser 'Dias da semana'.
        """
        self.assertEqual(Weekdays._meta.verbose_name_plural, 'Dias da semana')


class ScheduleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando um objeto Schedule para uso nos testes
        Schedule.objects.create(time=time(hour=8, minute=30))

    def test_str_method(self):
        """
        O método __str__() de Schedule deve retornar o horário formatado.
        """
        schedule = Schedule.objects.get(time=time(hour=8, minute=30))
        self.assertEqual(str(schedule), '08:30:00')

    def test_verbose_name(self):
        """
        O verbose_name da classe Meta em Schedule deve ser 'Horário'.
        """
        self.assertEqual(Schedule._meta.verbose_name, 'Horário')

    def test_verbose_name_plural(self):
        """
        O verbose_name_plural da classe Meta em Schedule deve ser 'Horários'.
        """
        self.assertEqual(Schedule._meta.verbose_name_plural, 'Horários')

class SystemConstantsConfigTest(TestCase):
    def test_default_auto_field(self):
        """
        Verifica se o default_auto_field é definido corretamente.
        """
        self.assertEqual(SystemConstantsConfig.default_auto_field, 'django.db.models.BigAutoField')

    def test_name(self):
        """
        Verifica se o nome da aplicação está correto.
        """
        self.assertEqual(SystemConstantsConfig.name, 'system_constants')

    def test_verbose_name(self):
        """
        Verifica se o verbose_name está definido corretamente.
        """
        self.assertEqual(SystemConstantsConfig.verbose_name, 'Constantes')

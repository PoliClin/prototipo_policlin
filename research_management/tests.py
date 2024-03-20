from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from rooms.models import Room
from system_constants.models import Schedule, Weekdays
from django.contrib.auth.models import User
from .models import Research, ScheduledTimes

from .forms import ResearchForm

from .apps import ResearchManagementConfig

from django.contrib.auth.models import User, Group
from django.contrib.admin.sites import AdminSite
from .models import Research, ScheduledTimes
from .forms import ResearchForm
from .admin import ResearchAdmin


from research_management.models import Research, ScheduledTimes

User = get_user_model()

class ResearchModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Cria mock do usuário Pesquisador Principal"""
        cls.main_researcher = User.objects.create_user(username='main_researcher', password='test000')
        """Cria mock dos usuários Pesquisadores"""
        cls.researcher1 = User.objects.create_user(username='researcher_1', password='test111')
        cls.researcher2 = User.objects.create_user(username='researcher_2', password='test222')
        
        """Cria mock de Pesquisa"""
        cls.research = Research.objects.create(
            name="Estudo sobre a disciplina Ambiente de Desenvolvimento de Software, 2023.2",
            main_researcher=cls.main_researcher,
            conep_approvement_date=date.today(),
            start_date=date.today(),
            ending_date=date.today() + timedelta(days=30),
            expected_number_of_patients=10,
            outpatient_care=True,
            is_active=True
        )
        cls.research.researchers.add(cls.researcher1, cls.researcher2)

    def test_research_creation(self):
        """Valida a criação da pesquisa e seus atributos principais."""
        self.assertEqual(self.research.name, "Estudo sobre a disciplina Ambiente de Desenvolvimento de Software, 2023.2")
        self.assertEqual(self.research.main_researcher, self.main_researcher)
        self.assertTrue(self.research.is_active)

    def test_research_dates(self):
        """Valida os atributos de data da pesquisa"""
        self.assertEqual(self.research.conep_approvement_date, date.today())
        self.assertEqual(self.research.start_date, date.today())
        self.assertTrue(self.research.ending_date > self.research.start_date)

    def test_research_researchers(self):
        """Valida se a criação dos pesquisadores foi bem sucedida."""
        self.assertTrue(self.research.researchers.filter(username='researcher_1').exists())
        self.assertTrue(self.research.researchers.filter(username='researcher_2').exists())
        self.assertEqual(self.research.researchers.count(), 2)


    def test_not_research_researchers(self):
        """Valida se a criação de um pesquisador impossível não foi bem sucedida."""
        self.assertFalse(self.research.researchers.filter(username='researcher_999').exists())


class ScheduledTimesModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Mocks principais para os testes da classe."""
        cls.user = User.objects.create_user(username='testuser', password='12345')

        cls.research = Research.objects.create(
            name="Estudo sobre Teste",
            main_researcher=cls.user,
            expected_number_of_patients=10,
        )

        cls.room = Room.objects.create(
            number=101,
            exam_collection_room=True,
        )

        cls.start_schedule = Schedule.objects.create(time="09:00")
        cls.end_schedule = Schedule.objects.create(time="17:00")
        cls.monday = Weekdays.objects.create(name="Segunda-feira")
        cls.tuesday = Weekdays.objects.create(name="Terça-feira")

        cls.scheduled_time = ScheduledTimes.objects.create(
            start_schedule=cls.start_schedule,
            end_schedule=cls.end_schedule,
            research=cls.research,
            room=cls.room,
        )
        cls.scheduled_time.weekday.add(cls.monday, cls.tuesday)

    def test_scheduled_time_creation(self):
        """Valida a criação correta do objeto de Pesquisa com horário marcado."""
        self.assertEqual(str(self.scheduled_time), f"{self.research} - {self.room}")
        self.assertTrue(self.scheduled_time.weekday.filter(name="Segunda-feira").exists())
        self.assertTrue(self.scheduled_time.weekday.filter(name="Terça-feira").exists())
        self.assertEqual(self.scheduled_time.start_schedule, self.start_schedule)
        self.assertEqual(self.scheduled_time.end_schedule, self.end_schedule)


    def test_invalid_weekday_scheduled_time_creation(self):
        """Valida objeto inexistente com dia de semana inválido."""
        self.assertFalse(self.scheduled_time.weekday.filter(name="Sábado").exists())

class ResearchFormTest(TestCase):
    def test_researchers_query_set(self):
        """
        Verifica se o queryset de 'researchers' está filtrando corretamente os usuários com 'pesquisador' no username.
        """
        form = ResearchForm()
        query_set = form.fields['researchers'].queryset
        self.assertTrue(all('pesquisador' in user.username for user in query_set))

    def test_main_researcher_query_set(self):
        """
        Verifica se o queryset de 'main_researcher' está filtrando corretamente os usuários com 'pesquisador' no username.
        """
        form = ResearchForm()
        query_set = form.fields['main_researcher'].queryset
        self.assertTrue(all('pesquisador' in user.username for user in query_set))


class ScheduledTimesFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='pesquisador1')
        self.research = Research.objects.create(name='Test Research')
        self.room = Room.objects.create(number='101')
    

class ResearchManagementConfigTest(TestCase):
    def test_default_auto_field(self):
        """
        Verifica se o default_auto_field é definido corretamente.
        """
        self.assertEqual(ResearchManagementConfig.default_auto_field, 'django.db.models.BigAutoField')

    def test_name(self):
        """
        Verifica se o nome da aplicação está correto.
        """
        self.assertEqual(ResearchManagementConfig.name, 'research_management')

    def test_verbose_name(self):
        """
        Verifica se o verbose_name está definido corretamente.
        """
        self.assertEqual(ResearchManagementConfig.verbose_name, 'Gerenciamento de Pesquisas')

class CustomAdminSite(AdminSite):
    def get_registered_model(self, model):
        """
        Retorna o modelo registrado no admin ou None se não estiver registrado.
        """
        if model == Group:
            return None
        return super().get_registered_model(model)

class ResearchAdminTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='researcher1')
        self.research = Research.objects.create(name='Test Research', main_researcher=self.user)

    def test_list_display(self):
        """
        Verifica se os campos especificados em list_display estão corretos.
        """
        self.assertEqual(ResearchAdmin.list_display, ('is_active', 'name', 'main_researcher', 'expected_number_of_patients', 'outpatient_care'))

    def test_list_filter(self):
        """
        Verifica se os campos especificados em list_filter estão corretos.
        """
        self.assertEqual(ResearchAdmin.list_filter, ('main_researcher',))

    def test_list_display_links(self):
        """
        Verifica se os campos especificados em list_display_links estão corretos.
        """
        self.assertEqual(ResearchAdmin.list_display_links, ('name',))

    def test_form(self):
        """
        Verifica se o formulário associado ao ResearchAdmin é o ResearchForm.
        """
        self.assertEqual(ResearchAdmin.form, ResearchForm)

from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Research

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


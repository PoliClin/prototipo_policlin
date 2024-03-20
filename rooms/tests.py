from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .apps import RoomsConfig
from .admin import RoomAdmin
from .models import Room


class RoomModelTest(TestCase):

    def setUp(self):
        """Cria uma sala 'mock' para os testes da classe."""
        Room.objects.create(number=999, exam_collection_room=True, archive_room=False)

    def test_room_creation(self):
        """Valida a criação do 'mock' e seus atributos."""
        room = Room.objects.get(number=999)
        self.assertEqual(room.exam_collection_room, True)
        self.assertEqual(room.archive_room, False)
        self.assertEqual(str(room), "Sala 999")

    def test_room_unique_number(self):
        """ Cria uma sala com um número específico e valida a constraint 'unique' 
            ao tentar criar outra de mesmo número.
        """
        Room.objects.create(number=102, exam_collection_room=False, archive_room=True)
        with self.assertRaises(Exception):
            Room.objects.create(number=102, exam_collection_room=True, archive_room=False)

    def test_room_fields_not_null(self):
        """ Valida a constraint 'not null' 
            ao tentar criar salas com atributos nulos.
        """
        with self.assertRaises(Exception):
            Room.objects.create(number=None)
        with self.assertRaises(Exception):
            Room.objects.create(number=103, exam_collection_room=None, archive_room=None)

class RoomAdminTest(TestCase):
    def setUp(self):
        self.admin_site = AdminSite()
        self.room_admin = RoomAdmin(Room, self.admin_site)

    def test_list_display(self):
        """
        Verifica se os campos especificados em list_display estão corretos.
        """
        self.assertEqual(self.room_admin.list_display, ('_number', 'exam_collection_room', 'archive_room'))

    def test_search_fields(self):
        """
        Verifica se os campos especificados em search_fields estão corretos.
        """
        self.assertEqual(self.room_admin.search_fields, ('number',))

    def test_list_filter(self):
        """
        Verifica se os campos especificados em list_filter estão corretos.
        """
        self.assertEqual(self.room_admin.list_filter, ('archive_room', 'exam_collection_room'))

    def test_number_display(self):
        """
        Verifica se o método _number exibe o número da sala corretamente.
        """
        # Criando um objeto Room para uso no teste
        room = Room(number='101')
        # Testando o método _number
        self.assertEqual(self.room_admin._number(room), 'Sala 101')

class RoomsConfigTest(TestCase):
    def test_default_auto_field(self):
        """
        Verifica se o default_auto_field é definido corretamente.
        """
        self.assertEqual(RoomsConfig.default_auto_field, 'django.db.models.BigAutoField')

    def test_name(self):
        """
        Verifica se o nome da aplicação está correto.
        """
        self.assertEqual(RoomsConfig.name, 'rooms')

    def test_verbose_name(self):
        """
        Verifica se o verbose_name está definido corretamente.
        """
        self.assertEqual(RoomsConfig.verbose_name, 'Gerenciamento de Salas')

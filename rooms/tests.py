# Create your tests here.
from django.test import TestCase

from .models import Room


class RoomModelTest(TestCase):

    def setUp(self):
        # mocked
        Room.objects.create(number=999, exam_collection_room=True, archive_room=False)

    def test_room_creation(self):
        room = Room.objects.get(number=999)
        self.assertEqual(room.exam_collection_room, True)
        self.assertEqual(room.archive_room, False)
        self.assertEqual(str(room), "Sala 999")

    def test_room_unique_number(self):
        Room.objects.create(number=102, exam_collection_room=False, archive_room=True)
        with self.assertRaises(Exception):
            Room.objects.create(number=102, exam_collection_room=True, archive_room=False)

    def test_room_fields_not_null(self):
        with self.assertRaises(Exception):
            Room.objects.create(number=None)
        with self.assertRaises(Exception):
            Room.objects.create(number=103, exam_collection_room=None, archive_room=None)

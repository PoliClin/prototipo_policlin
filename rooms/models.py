from django.conf import settings
from django.db import models


class RoomStatus(models.TextChoices):
    OCCUPIED = 'Ocupada', 'Ocupada'
    AVAILABLE = 'Disponível', 'Disponível'

class Room(models.Model):
    number = models.IntegerField(verbose_name="Número da sala", null=False, blank=False, unique=True)
    status = models.CharField(max_length=10, choices=RoomStatus.choices, default=RoomStatus.AVAILABLE, verbose_name="Status")
    exam_collection_room = models.BooleanField(verbose_name="Coleta de Exames", default=False, null = False, blank= False)
    archive_room = models.BooleanField(verbose_name="Arquivos", default=False, null = False, blank= False)


    def __str__(self):
        return f"Sala {self.number}"
    
    class Meta:
        verbose_name = "Salas"
        verbose_name_plural = "Salas"

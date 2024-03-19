from django.db import models


class Weekdays(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Dia da semana")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Dia da semana"
        verbose_name_plural = "Dias da semana"
    

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField(verbose_name="Horário")

    def __str__(self):
        return str(self.time)
    
    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"

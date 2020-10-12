from django.db import models

from api.enums import EquipmentStatus


class Vessel(models.Model):
    code = models.CharField('Vessel code', max_length=20, primary_key=True)

    def __str__(self):
        return f'Vessel {self.code}'


class Equipment(models.Model):
    code = models.CharField('Equipment code', max_length=20, primary_key=True)
    name = models.CharField('Equipment name', max_length=50)
    location = models.CharField('Equipment location', max_length=50)
    status = models.CharField(
        'Equipment status', max_length=20, choices=EquipmentStatus.choices(),
        default=EquipmentStatus.active
    )

    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Equipment {self.code} - {self.status.name}'

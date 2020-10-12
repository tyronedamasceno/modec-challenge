from django.db import models


class Vessel(models.Model):
    code = models.CharField('Vessel code', max_length=20, primary_key=True)

    def __str__(self):
        return f'Vessel {self.code}'

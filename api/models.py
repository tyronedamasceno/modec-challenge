from django.db import models


class Vessel(models.Model):
    code = models.CharField('Vessel Code', max_length=20, unique=True)

    def __str__(self):
        return f'Vessel {self.code}'

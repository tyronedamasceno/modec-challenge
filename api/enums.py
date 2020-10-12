from collections import namedtuple
from enum import Enum

choice = namedtuple('Choice', 'name value')


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [choice(e.value, e.name) for e in cls]


class EquipmentStatus(ChoiceEnum):
    active = "ACTIVE"
    inactive = "INACTIVE"

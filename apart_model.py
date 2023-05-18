from pydantic import BaseModel, ValidationError, validator
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from dataclasses import dataclass as _basemodel_decorator
else:
    _basemodel_decorator = lambda x: x


@_basemodel_decorator
class ApartModel(BaseModel):
    build_tech: int
    floor: int
    area: int
    rooms: int
    balcon: int
    metro_dist: float

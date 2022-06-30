import datetime
from ninja import Schema, Path
from typing import List
from pydantic import Field


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.day)


class Filters(Schema):
    limit: int = 100
    offset: int = None
    query: str = None
    category__in: List[str] = Field(None, alias="categories")

class Item(Schema):
    name: str
    description: str = None
    price: float
    quantity: int
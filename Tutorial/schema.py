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

class UserSchema(Schema):
    id: int
    first_name: str
    last_name: str

class TaskSchema(Schema):
    id: int
    title: str
    is_completed: bool
    owner: UserSchema = None  # ! None - to mark it as optional

class User(Schema):
    id: int
    first_name: str
    last_name: str

class UserIn(Schema):
    username: str
    password: str


class UserOut(Schema):
    id: int
    username: str

##
class Token(Schema):
    token: str
    expires: datetime.date

class Message(Schema):
    message: str

class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: datetime.date = None

class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: datetime.date = None

class DepartmentIn(Schema):
    id: int
    title: str

class UserSchema(Schema):
    id: int
    name: str
    email: str = None
